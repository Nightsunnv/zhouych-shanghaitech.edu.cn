#=============================================================================#
#                            Homework 4: yourSQL                              #
#         SI 100B: Introduction to Information Science and Technology         #
#                     Spring 2020, ShanghaiTech University                    #
#                     Author: Diao Zihao <hi@ericdiao.com>                    #
#                         Last motified: 02/18/2020                           #
#=============================================================================#
# Implement your database here.
def takeKeys(elem):
    return elem[0]


class Row():
    """
    The `Row` class.

    You are building the row class here.
    """

    def __init__(self, keys, data, primary_key=None):
        self.dict = {}
        self.priiimarykey = primary_key
        if primary_key == None:
            self.priiimarykey = keys[0]
        if primary_key != None and primary_key not in keys:
            raise KeyError
        if type(keys) != list or type(data) != list:
            raise TypeError
        if len(keys) == 0 or len(data) == 0:
            raise ValueError
        if len(keys) != len(data):
            raise KeyError
        for i in range(len(keys)):
            self.dict[keys[i]] = data[i]
        ## YOUR CODE HERE ##

    def __getitem__(self, key):
        if key in self.dict:
            return self.dict[key]
        else:
            raise KeyError
        ## YOUR CODE HERE ##

    def __setitem__(self, key, value):
        if key in self.dict:
            self.dict[key] = value
        else:
            raise KeyError
        ## YOUR CODE HERE ##

    def __iter__(self):
        return iter(sorted(self.dict))
        ## YOUR CODE HERE ##

    def __next__(self):
        return next(self)#怎么写？
        ## YOUR CODE HERE ##

    def __len__(self):
        return len(self.dict)
        ## YOUR CODE HERE ##

    def __lt__(self, other):
        if type(other) != Row:
            raise TypeError
        if len(self.dict) != len(other.dict):
            raise TypeError
        if self.get_primary_key() != other.get_primary_key():
            raise TypeError
        primKey = self.get_primary_key()
        if self.dict[primKey] >= other.dict[primKey]:
            return False
        else:
            return True

        ## YOUR CODE HERE ##

    def keys(self):
        return list(self.dict.keys()).sort()
        ## YOUR CODE HERE ##

    def get_primary_key(self):
        return str(self.priiimarykey)
        ## YOUR CODE HERE ##


class Table():
    """
    The `Table` class.

    This class represents a table in your database. The table consists
    of one or more lines of rows. Your job is to read the content of the table
    from a CSV file and add the support of iterator to the table. See the
    specification in README.md for detailed information.
    """

    def __init__(self, filename, rows=None, keys=None, primary_key=None):
        self.list = []
        self.name = filename
        if rows != None and keys != None and len(rows) != 0 and len(keys) != 0:
            for i in rows:
                self.list.append(Row(keys, i, primary_key))
        else:
            f = open(filename, mode='r+')
            q = f.readlines()
            temp = 0
            lenn = len(q)
            for i in range(len(q)):
                q[i] = q[i].replace("\n", "")
            while temp < lenn:
                if q[temp].isspace():
                    del q[temp]
                    lenn -= 1
                    continue
                else:
                    temp += 1
                    continue
            for i in range(len(q)):
                q[i] = q[i].split(",")
                for j in range(len(q[i])):
                    q[i][j] = q[i][j].strip()
            for i in q[1:]:
                self.list.append(Row(q[0], i, primary_key))

        ## YOUR CODE HERE ##

    def __iter__(self):
        return iter(self.list)
        ## YOUR CODE HERE ##

    def __next__(self):
        return next(self)
        ## YOUR CODE HERE ##

    def __getitem__(self, key):
        primaryKey = self.get_primary_key()
        for i in self.list:
            if i.dict[primaryKey] == str(key):
                mmp = Row(list(i.dict.keys()), list(i.dict.values()), primaryKey)
                return mmp
        else:
            raise ValueError
        ## YOUR CODE HERE ##

    def __len__(self):
        return len(self.list)+1
        ## YOUR CODE HERE ##

    def get_table_name(self):
        return self.name
        ## YOUR CODE HERE ##

    def keys(self):
        return list(self.list[0].keys())
        ## YOUR CODE HERE ##

    def get_primary_key(self):
        return self.list[0].get_primary_key()
        ## YOUR CODE HERE ##

    def export(self, filename=None):
        pass
        ## YOUR CODE HERE ##


class Query():
    """
    The `Query` class.
    """

    def __init__(self, query):
        pass
        ## YOUR CODE HERE ##

    def as_table(self):
        pass
        ## YOUR CODE HERE ##


class JoinQuery(Query):
    """
    The `JoinQuery` class
    """


class AggQuery(Query):
    """
    The `AggQuery` class
    """


if __name__ == '__main__':
    table = Table('testcases/student.csv')
    print([row['id'] for row in table])
    row = table['45280742']
    print(row.dict)
