#!/usr/bin/python3
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

builder = Gtk.Builder()
builder.add_from_file('./words.glade')

window = builder.get_object('mainWin')
tstore = builder.get_object('treestore1')
tstore.append(None,['qwe','asd','zxc','rty',True])
window.show_all()

Gtk.main()