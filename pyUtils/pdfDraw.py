#!/usr/bin/env python
# encoding: utf-8

import ROOT as r

# a wrapper for canvas.Print()
# outputs as a multi page PDF

class printPDF(object):
  """docstring for printPDF"""
  def __init__(self, Fname):
    super(printPDF, self).__init__()
    self.canvas = r.TCanvas()
    self.fname = Fname
    self.pageCounter = 1


  def cd(self):
    """cd to the self.canvas object"""
    self.canvas.cd()
    pass


  def open(self):
    """open the output file"""
    self.canvas.Print(self.fname+"[")
    pass


  def close(self):
    """close the output file"""
    self.canvas.Print(self.fname+"]")
    pass


  def Clear(self):
    """Wrap Clear"""
    self.canvas.Clear()
    pass

  def SetLog(self,axis,BOOL):
    """Wrap SetLog"""
    if 'x' in axis:
      if BOOL:
        self.canvas.SetLogx()
      else:
        self.canvas.SetLogx(r.kFALSE)
    if 'y' in axis:
      if BOOL:
        self.canvas.SetLogy()
      else:
        self.canvas.SetLogy(r.kFALSE)
    pass


  def Print(self):
    """Wrap Print Print, inciment page number"""
    num = r.TLatex(0.95,0.01,"%d"%(self.pageCounter))
    num.SetNDC()
    num.Draw("same")
    self.canvas.SetGridx()
    self.canvas.SetGridy()
    self.canvas.Print(self.fname)
    self.pageCounter += 1
    pass