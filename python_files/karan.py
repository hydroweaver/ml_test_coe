#!/usr/bin/env python
import tensorflow as tf

print(tf.__version__)

print("THIS IS RUNNING")

def square(s):
	return(s*s)

print(square(10))
