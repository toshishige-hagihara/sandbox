class VmstatData(object):
    COLUMNS=['r', 'b',
             'swpd', 'free', 'buff', 'cache',
             'si', 'so',
             'bi', 'bo',
             'in', 'cs',
             'us', 'sy', 'id', 'wa']

    def __init__(self, coltype=None):
        if coltype is None:
            coltype = VmstatData.COLUMNS
        self._coltype = coltype
        self._cols = []
        self._col_max = []
        for i in range(len(self._coltype)):
            self._cols.append([])

    def __getattr__(self, name):
        if name in self._coltype:
            idx = self._coltype.index(name)
            return self._cols[idx]
        if name.endswith('_max') and name[:-4] in self._coltype:
            idx = self._coltype.index(name[:-4])
            return self._col_max[idx]
        return None

    def cols(self):
        return self._cols

    def load(self, f):
        for line in f:
            cols = line.split()
            if len(filter(lambda x: not x.isdigit(), cols)) > 0:
                continue
            if len(cols) != len(self._coltype):
                raise RuntimeError('Column Type does not match:\n %s' % ', '.join(self._coltype))
            for i, col in enumerate(cols):
                self._cols[i].append(int(col))
        for col in self._coltype:
            self._col_max.append(max(self.__getattr__(col)))
