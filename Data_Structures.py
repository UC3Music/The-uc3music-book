# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 14:56:52 2020

@author: ldcas
"""

import re

class Chord():
    """
    DS representation of a chord.
    
    ATTRIBUTES
    ----------
    name : str
        Chord name.
    root : str (len = 1)
        Root note of the chord.
    duration : float (0 < duration < maxDurationOfBar)
        Duration of the chord.
        whole note = 1
        half note = 0.5
        quarter note = 0.25
        etc.
    """
    
    def __init__(self, name: str, duration):
        self.name = name
        self.root = self.__root_recognition(name)
        self.duration = duration

    def __root_recognition(self, chord):
        
        if re.search("/", chord) is None:
            return chord[0]
        else:
            return chord[-1]
    
class Bar():
    """
    DS representation of a bar.
    
    ATTRIBUTES
    ----------
    pos : int
        Bar position.
    measure : str ("X:Y")
        Measure of the bar.
    maxDuration : float
        Maximum duration (in whole notes) of the bar.
    chords : list ([Chord, ...])
        Chords in the bar.
    """
    
    def __init__(self, pos, measure : str):
        self.pos = pos
        self.measure = measure
        self.maxDuration = self.__maxDurCalc(measure)
        self.chords = []
        
        self.__buffer = 0
        
    def __maxDurCalc(self, measure):
        split = re.split(":", measure)
        
        return int(split[0])/int(split[1])
    
    def addChord(self, chord : Chord, duration):
        pass
    
class Section():
    
    def __init__(self, name : str):
        self.name = name
        self.bars = []
        
        # self.__buffer = 0
        
    def addChord(self, chord : Chord):
        pass

        
class Song():
    
    def __init__(self, title, author, year, img):
        self.title = title
        self.author = author
        self.year = year
        self.img = img
        self.bars
        
        self.sections = []
        
    def addSection(self, name : str):
        section = Section(name)
        self.sections.append(section)
    
    def updateBars(self):
        for sec in self.sections:
            self.bars += sec.bars






