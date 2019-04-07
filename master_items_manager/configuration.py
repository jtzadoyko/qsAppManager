# -*- coding: utf-8 -*-
# @Author: jtzadoyko
# @Date:   2019-03-09 23:42:09
# @Last Modified by:   jtzadoyko
# @Last Modified time: 2019-04-06 22:19:29


import pandas as pd
import os


class qsConfiguration:

    def __init__(self, targetFile, targetSheet, targetLocation=False):
        self.trgfile = str(targetFile)
        self.trgSheet = str(targetSheet)
        self.trgLoc = str(targetLocation)

        if self.trgLoc:
            self.trgFp = os.path.join(os.getcwd(), self.trgfile)
        else:
            self.trgFp = os.path.join(self.trgLoc, self.trgfile)

        self.exists = os.path.isfile(self.trgFp)

        if self.exists:
            try:
                self.df = pd.read_excel(self.trgFp, self.trgSheet)
            except:
                self.df = False
        else:
            self.df = False

        if isinstance(self.df, (bool)):
            self.fields = False
        else:
            self.fields = list(self.df.columns.values)

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
