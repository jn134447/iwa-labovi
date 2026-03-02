import socket


def init_server(ip: str, port: int) -> socket.socket:
    s = socket.socket()
    s.bind((ip, port))
    s.listen()
    return s


s = init_server("127.0.0.1", 8000)

while True:
    c, addr = s.accept()
    print(c.recv(1034).decode())
    print(addr)
    body = """
        <html>
            <body>
                <p>ectetur lorem efficitur sit amet. Nam magna ex, mollis sit amet facilisis eu, tempus eget odio. In et odio vitae quam ullamcorper feugiat et ut orci. Aenean dignissim ligula et eros lobortis, ac sodales lorem efficitur. Sed sit amet risus condimentum, pellentesque diam quis, porttitor leo. Cras facilisis felis dui, quis sagittis lorem dictum vel.

Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Nullam pretium tellus sed efficitur eleifend. Etiam eleifend mollis elementum. Duis cursus varius est. Aliquam erat volutpat. Integer vehicula elit at congue aliquet. Suspendisse vel fermentum ipsum. Fusce porttitor eros et lectus blandit elementum. Aliquam sit amet hendrerit sapien.

Phasellus tempus, augue non imperdiet tincidunt, ipsum quam consectetur dolor, eget sollicitudin eros turpis suscipit mi. Donec ut dictum purus, a venenatis nulla. Fusce at felis leo. Curabitur dui enim, accumsan non nisl non, porttitor sollicitudin ex. In vel dui ligula. Cras ultricies ut magna maximus vulputate. Nam at placerat mauris. In eget odio eget urna maximus varius eget eget orci. Proin metus nisl, laoreet ac interdum et, placerat feugiat mi.

Nunc hendrerit porta odio. Vestibulum in egestas nisl. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nullam convallis diam vitae metus pharetra, in ullamcorper orci efficitur. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Curabitur condimentum turpis feugiat quam feugiat finibus. Nam luctus aliquet elementum. Quisque varius a velit sit amet convallis. Integer vel tortor eget dui dapibus feugiat eu eget purus. Quisque erat nisl, vestibulum ut porta at, aliquam cursus leo. Nunc quis ex at arcu auctor mollis. Nulla facilisi.

Proin id justo at tortor venenatis ornare. Vestibulum imperdiet rutrum hendrerit. Duis pulvinar lacinia quam, eu dignissim sem commodo ac. Donec quis sapien nec metus tristique efficitur id sed enim. Morbi sit amet rutrum justo, ut bibendum nunc. Nunc turpis dolor, vulputate eget fringilla at, condimentum quis ante. Sed laoreet nunc mauris, sit amet luctus nisl condimentum sit amet. Donec ac lacus id ligula dignissim blandit et sit amet leo. In felis tellus, volutpat ut tempus a, iaculis vitae mi. Quisque et vehicula sapien. Vestibulum viverra nulla est, at aliquet ex feugiat ut.

Phasellus sed sem iaculis, commodo urna at, finibus nulla. Donec quis elementum sapien. Vestibulum volutpat ut nunc nec imperdiet. Pellentesque non cursus neque. Nulla facilisi. Etiam eget quam vehicula, consequat mauris semper, egestas nisi. Aliquam erat volutpat.

Cras id iaculis diam. Maecenas cursus consectetur arcu. Suspendisse semper, lacus vel sollicitudin mattis, est augue molestie nisi, eget lobortis nisi odio et massa. Suspendisse sodales feugiat nisl, eu lacinia sapien dapibus et. Sed odio est, mattis a erat vitae, convallis sollicitudin magna. Nulla eget leo ut tortor efficitur fermentum. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Vivamus dictum tempus tempor. Sed a mollis nibh. Quisque ultrices auctor ex.

Quisque dapibus neque enim, ut vehicula odio porta at. Ut mattis maximus urna, non cursus lacus suscipit quis. Phasellus cursus ultricies turpis aliquet suscipit. Aliquam faucibus et turpis viverra posuere. Praesent sagittis turpis ac augue elementum, in convallis metus feugiat. Morbi aliquet pulvinar arcu. Fusce quis odio pulvinar, scelerisque tellus vitae, rhoncus quam. Maecenas in nunc mi. Phasellus ut mauris lacus. Phasellus malesuada quam ligula, non mattis dolor rhoncus non.

Integer facilisis semper ultricies. Integer fringilla vestibulum turpis sit amet volutpat. Mauris sed maximus mi. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Cras blandit quam eu sem sodales, in porttitor ipsum placerat. Donec a lacus nec ante efficitur vehicula. Suspendisse at dolor egestas, semper lorem a, convallis leo.

Donec mattis mi vitae mollis euismod. Mauris et condimentum nibh, eget ornare eros. Nullam eget lectus aliquet, placerat diam non, molestie ex. Etiam nisl elit, tempus vel aliquet eu, dignissim eu dui. Suspendisse quis massa sed purus efficitur lacinia. Nullam vestibulum finibus eleifend. Nunc sit amet consectetur eros. Etiam mattis, velit eleifend interdum vulputate, est diam porttitor velit, ac placerat nisl velit eget ligula. Nam feugiat porta eros, a porttitor lacus sodales et. </p>
            </body>
        </html>
    """
    CRLF = "\r\n"
    header = "HTTP/1.1 200 OK"
    response = header + CRLF + CRLF + body
    c.send(response.encode())
    c.close()
    print("------------------------")
