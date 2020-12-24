# -*- coding=utf-8 -*-
 
import pyodbc
from   datetime import datetime
import pymssql
import os
import decimal
import config
import argparse

class SQLServer:
    def __init__(self,server,user,password,database,autocommit):
        self.server = server
        self.user = user
        self.password = password
        self.database = database
        self.autocommit = autocommit
 
    def __GetConnect(self):
        if not self.database:
            raise(NameError,"没有数据库信息")
        self.conn = pymssql.connect(server=self.server,user=self.user,password=self.password,database=self.database,autocommit=self.autocommit)
        cur = self.conn.cursor()
        if not cur:
            raise(NameError,"连接数据库失败")
        else:
            return cur
     
    def backup_db(self,database=config.db_name,back_root_dir=config.back_root_dir):
        cur = self.__GetConnect()
        backPath = os.path.join(back_root_dir ,"%s_%s.bak"%( database , datetime.now().strftime("%Y%m%d") ) )
        if not os.path.exists(backPath):
            os.mkdir(backPath)
        #sql = "BACKUP DATABASE [{0}] TO DISK = N'{1}'".format(database,backPath)
        sql = "BACKUP DATABASE [{0}] TO DISK = '{1}'".format(database,backPath)
        cur.execute(sql)
        self.conn.close()

    def recover_db(self,config.db_name,backpath)
        backPath = backpath + database + datetime.now().strftime("%Y%m%d") + '.bak'
        sql = "Restore  DATABASE [{0}] From DISK = '{1}'".format(database,backPath)
        cur.execute(sql)
        self.conn.close()

    def list_bakcup(self,back_root_dir=config.back_root_dir)
        for f in os.listdir(back_root_dir):
            if os.path.isfile(f):
                print (f)


    def ExecQuery(self,sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()

def parse():
    parser = argparse.ArgumentParser(prog=sys.argv[0], description=__d
    parser.add_argument("--recover",
                        action='store_true',
                        help ="恢复模式")
    parser.add_argument("--backup",
                        action='store_true',
                        help ="备份模式")
    parser.add_argument("--list",
                        action='store_true',
                        help ="查询备份文件")
    parser.add_argument("--file",
                        help='指定数据库的备份文件路径')
    parser.set_defaults(recover=False)
    parser.set_defaults(backup=False)
    parser.set_defaults(list=True)
    args=parser.parse_args()
    return args


def main():
    args=parse()
    msg = SQLServer(server=config.server_ip,user=config.db_admin,password=config.db_admin_pass,database=config.db_name,autocommit=True)
    if args.backup:
        msg.backup_db()
        sys.exit(0)
    elif args.recover:
        msg.recover_db(args.file)
        sys.exit(0)
    elif args.list:
        msg.list_backup()
        sys.exit(0)
 
 
if __name__ == "__main__":
    main()