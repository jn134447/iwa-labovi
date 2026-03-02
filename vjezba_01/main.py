import socket


def connect_to_server(ip: str, port: int, max_attempts=5) -> socket.socket:
    s = socket.socket()
    try:
        s.connect((ip, port))
    except Exception as e:
        print(f"Error connecting socket: {e}")

    return s


def retrieve_source(s: socket.socket, ip: str, page: str) -> str:
    request = f"GET {page} HTTP/1.1\r\nHost: {ip}\r\nConnection: close\r\n\r\n"

    # try except blocks cause i dont want to halt crawling
    # beucase of websites being "unique"
    try:
        s.send(request.encode())
    except Exception:
        return b"".decode()

    response = b""
    while True:
        chunk = s.recv(4096)
        if not chunk:
            break
        response += chunk

    try:
        return response.decode()
    except Exception:
        return b"".decode()


def filter_links(src: str) -> list[str]:
    links = []
    beg = 0
    beg_str = 0
    while True:
        beg_str = src.find("href", beg)
        # beg_str = src.find("HREF", beg)
        if beg_str == -1:
            return links

        beg_str = src.find("=", beg_str)
        if beg_str == -1:
            return links

        beg_str = src.find('"', beg_str)
        if beg_str == -1:
            return links

        end_str = src.find('"', beg_str + 1)
        link = src[beg_str + 1 : end_str]
        if link not in links:
            links.append(link)
        beg = end_str + 1


def validate_links(links: list[str]) -> list[str]:
    rem = []
    for link in links:
        if not link.startswith("http://"):
            rem.append(link)
    for rlink in rem:
        links.remove(rlink)

    return links


def run_crawler(
    links: list[str], max_links: int, port: int = 80, page: str = "/"
) -> list[str]:
    visited = []
    i = 0
    while i < len(links):
        link = links[i]

        print(f"connecting to: {link}")
        s = connect_to_server(link, port)

        page_src = retrieve_source(s, link, page)

        s.close()
        visited.append(link)

        new_links = filter_links(page_src)
        new_links = validate_links(new_links)

        for nlink in new_links:
            nlink = nlink.lstrip("http://")
            nlink = nlink.split("/")[0]

            if nlink not in links:
                print("new: ", nlink)
                links.append(nlink)

                if len(links) >= max_links:
                    print("hit max_links!")
                    return links

        i += 1

    return links


# links = ["wtarreau.free.fr", "1wt.eu", "www.productontology.org", "www.sekonix.com"]
links = ["www.productontology.org"]
# links = ["www.poslovniforum.hr"]
# links = ["pmgsc.teletalk.com.bd"]
# links = ["www.hypercubeusa.com"]

# port = 80
# page = "/"

retlinks = run_crawler(links, 22)
print("----------")
print(retlinks)
print(len(retlinks))
