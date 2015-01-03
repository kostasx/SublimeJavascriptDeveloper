#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Kostas X Minaidis (Based on the work by: Myles McNamara, Matthias Krok and Eric Martel)
# @Date:   2015-01-03 
# @Author URL: https://github.com/kostasx
# @Plugin URL: https://github.com/kostasx/SublimeJavascriptDeveloper
# @License: GPL 3+

# available commands
#   javascript_developer_open_selection
#   javascript_developer_search_selection
#   javascript_developer_search_from_input

import sublime
import sublime_plugin
import subprocess
import webbrowser

def OpenInBrowser(url):
    webbrowser.open_new_tab(url)

def SearchMDN(text):
    url = 'https://developer.mozilla.org/en-US/search?q=' + text.replace(' ','%20')
    OpenInBrowser(url)

class JavascriptDeveloperSearchSelectionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for selection in self.view.sel():
            # if the user didn't select anything, search the currently highlighted word
            if selection.empty():
                selection = self.view.word(selection)

            text = self.view.substr(selection)
            SearchMDN(text)

class JavascriptDeveloperSearchFromInputCommand(sublime_plugin.WindowCommand):
    def run(self):
        # Get the search item
        self.window.show_input_panel('Search MDN for', '',
            self.on_done, self.on_change, self.on_cancel)
    def on_done(self, input):
        SearchMDN(input)

    def on_change(self, input):
        pass

    def on_cancel(self):
        pass