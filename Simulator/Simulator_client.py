import rpyc


class lemonator:
    def lemonator(p):
        connection = rpyc.connect("localhost", port=18861)
        rpyc.BgServingThread(connection)
        connection.root.run()
        return connection.root.get_lemonator()