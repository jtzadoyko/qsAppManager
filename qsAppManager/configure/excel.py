# -*- coding: utf-8 -*-
# @Author: jtzadoyko
# @Date:   2019-03-09 23:42:09
# @Last Modified by:   jtzdoyko
# @Last Modified time: 2019-04-08 20:41:00


import pandas as pd
import os
from base import baseConfig


class excelConfig(baseConfig):
    """initializing a configuration file 

    TODO:
        determine if the file path specified was placed within the qlik directory
        

    Args:
        tfile  :| baseConfig class
        tloc  ::| baseConfig class
        tsheet :|

    Attributes:
        tfile ::::| passing the name of the file to be read into
        tloc :::::| passing the absolute file path for the file
        tpath ::::| generating the file path from tloc and tfile
        is_valid :| determing if the file path was valid - returning bool

    """
    def __init__(self, tfile, tloc, tsheet):
        super().__init__(tfile, tloc)
        self.filetype = 'Excel'
        self.tsheet = tsheet

        if self.is_valid:
            try:
                self.df = pd.read_excel(self.tpath, self.tsheet)
                self.fields = list(self.df.columns.values)
            except:
                self.df = None
                self.fields = []
        else:
            self.df = None
            self.fields = []

    def valid_var_stup(self):
        if {'Name', 'Definition', 'Tags'}.issubset(self.fields):
            return True
        else:
            return False

    def valid_mi_stup(self):
        if {'Name', 'Expression', 'Label', 'Color', 'Tags'}.issubset(self.fields):
            return True
        else:
            return False



x = excelConfig(tfile = 'a',tloc = 'b', tsheet = 'c')
print(x.tfile)
print(x.tloc)
print(x.tpath)
print(x.is_valid)
print(x.filetype)
print(x.df)
print(x.fields)
print(x.valid_var_stup())
print(x.valid_mi_stup())