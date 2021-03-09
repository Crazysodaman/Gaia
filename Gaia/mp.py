import multiprocessing as mp
import cfg


if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=Kfilter.kalmanY, args=(child_conn,))
    p.start()
    print(parent_conn.recv())   # prints "[42, None, 'hello']"
    p.join()
