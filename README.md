jmad [![Build Status](https://travis-ci.org/kcharvey/jmad.svg?branch=master)](https://travis-ci.org/kcharvey/jmad)
===========

The Jazz Musicianship Archive and Database

Development
=======

Here's a little guidance if you're interested in helping out with the project.

Django Project Structure
-----

### people

This app takes care of all the humans in the project, be they personnel on 
recordings, composers, lyricits, managers, or just regular site users. Note
that these delineations can overlap. 

### solos

Information about snippets of recordings to which we can apply metadata and 
tags. Also instruments for convenience.

### tags

A generic-y implementation of a tagging system. These tags will be used across
models in other apps.

### tunes

This is a bit of a catch all app, but it's all centered around composed music.
Songs, recorded versions of those songs, albums, record labels, etc.
 
