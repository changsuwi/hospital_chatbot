class CaseInsensitiveDict(dict):
    def get(self, key, default=None):
        return super(CaseInsensitiveDict, self).get(key, default)

    def __getitem__(self, key):
        return super(CaseInsensitiveDict, self).__getitem__(key.lower())

    def __setitem__(self, key, value):
        super(CaseInsensitiveDict, self).__setitem__(key.lower(), value)

    def __contains__(self, key):
        return super(CaseInsensitiveDict, self).__contains__(key.lower())
