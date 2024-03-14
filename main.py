from GNSMQLParser import GNSMQLParser

dbPath = "/"

gnsmql = GNSMQLParser(dbPath)

gnsmql.execute("CREATE DATABASE test_db")
