#!/usr/bin/python3
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from words import *

def set_question(_,path,new_text):
    iter = tstore.get_iter(path)
    rendered=render(new_text)
    if not tstore.iter_depth(iter):
        tstore.set(iter,[0,1,2],[rendered['prefix'],'*'*rendered['num'],rendered['sufix']])
        leters=find_letters(**rendered, dictionary=res_dict)
        for leter in leters:
            tstore.append(iter, [rendered['prefix']+leter, leter, leter+rendered['sufix'], True, False, True])

def switch_use(_,path):
    iter = tstore.get_iter(path)
    # Get value at 2nd column
    if tstore.iter_depth(iter): tstore.set_value(iter,3,not tstore.get_value(iter, 3))

def add_line(_):
    tstore.append(None,['','','',True,True,False])

def rm_line(_):
    tmp_model, path = tree.get_selection().get_selected()
    if not (path is None): tstore.remove(path)

def solve(_):
    top_list = []
    rootiter = tstore.get_iter_first()
    while rootiter is not None:
        cur_list = []
        childiter = tstore.iter_children(rootiter)
        while childiter is not None:
            if tstore[childiter][3]: cur_list.append(tstore[childiter][1])
            childiter=tstore.iter_next(childiter)
        top_list.append(cur_list)
        rootiter = tstore.iter_next(rootiter)
    builder.get_object('resText').set_text('\n'.join(find_word(*top_list, dictionary=res_dict)))

f = open('./res_dict.txt','r')
res_dict = set(word.strip() for word in f)
f.close()

#res_buf = builder.get_object('resText')
#res_buf.set_text('123')

builder = Gtk.Builder()
builder.add_from_file('./words.glade')
window = builder.get_object('mainWin')
tree = builder.get_object('tree')
tstore = builder.get_object('treestore1')

builder.get_object('prefix_column').connect('edited',set_question)
builder.get_object('add_button').connect('clicked',add_line)
builder.get_object('rm_button').connect('clicked',rm_line)
builder.get_object('exe_button').connect('clicked',solve)
builder.get_object('use_flag').connect('toggled',switch_use)

window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()