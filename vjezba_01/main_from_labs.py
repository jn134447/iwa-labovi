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
        print("encode err")
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
        print("decode err")
        return b"".decode()


def get_links(src: str) -> list[str]:
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


def get_valid_links(links: list[str]) -> list[str]:
    rem = []
    for link in links:
        if not link.startswith("http://"):
            rem.append(link)
    for rlink in rem:
        links.remove(rlink)

    return links


def got_valid_response(src: str) -> bool:
    found = src.find("200 OK")
    if found < 0:
        return False
    else:
        return True


def run_crawler(
    ip: str, max_visited_pages: int, port: int = 80, page: str = "/"
) -> list[str]:
    visited_pages = []
    pages = []
    pages.append(page)

    i = 0
    while i < len(pages):
        page = pages[i]

        # socket has to be recreated on each loop cause the server closes it after receiving data from server
        # without "Connection: close" in the retrieve_source(), it hangs.
        # on windows it threw an error while debugging, while on linux it silently failed, weird.
        s = connect_to_server(ip, port)

        print(f"CHECKING PAGE [{len(visited_pages)}]: {page}")
        page_src = retrieve_source(s, ip, page)
        if not (got_valid_response(page_src)):
            print("didn't get valid response")
            s.close()
            i += 1
            continue

        # print(page_src)

        visited_pages.append(page)
        if len(visited_pages) >= max_visited_pages:
            print("hit threshold!")
            return pages

        new_links = get_links(page_src)
        # new_links = get_valid_links(new_links)

        for npath in new_links:
            if npath not in pages:
                print(f"\tnew [{len(pages)}]: {npath}")
                pages.append(npath)

        s.close()
        i += 1

    return pages


# links = ["wtarreau.free.fr", "1wt.eu", "www.productontology.org", "www.sekonix.com"]
# links = ["www.productontology.org"]
ip = "crawler-test.com"
# links = ["www.poslovniforum.hr"]
# links = ["pmgsc.teletalk.com.bd"]
# links = ["www.hypercubeusa.com"]

# port = 80
# page = "/"

retpages = run_crawler(ip, 50)
print("----------")
print(retpages)
print(len(retpages))
