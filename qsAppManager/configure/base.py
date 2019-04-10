# -*- coding: utf-8 -*-
# @Author: jtzadoyko
# @Date:   2019-03-09 23:42:09
# @Last Modified by:   jtzdoyko
# @Last Modified time: 2019-04-09 21:27:25


import os


class baseConfig:
    """initializing a configuration file 

    TODO:
        determine if the file path specified was placed within the qlik directory
        determine the file type and delimiter


    Args:
        tfile :| type(str)
        tloc ::| type(str)

    Attributes:
        tfile ::::| passing the name of the file to be read into
        tloc :::::| passing the absolute file path for the file
        tpath ::::| generating the file path from tloc and tfile
        is_valid :| determing if the file path was valid - returning bool

    """

    def __init__(self, tfile, tloc=os.getcwd()):
        self.tfile = tfile
        self.tloc = tloc
        self.tpath = os.path.join(self.tloc, self.tfile)
        self.is_valid = os.path.isfile(self.tpath)
