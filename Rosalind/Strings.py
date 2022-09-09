# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 10:39:41 2017

@author: Willian
"""

#Rosalind - Strings and lists
#
## Problem:
#
#Given: A string ss of length at most 200 letters and four integers aa, bb, 
# cc and dd.
#Return:The slice of this string from indices aa through bb and cc through
# dd (with space in between), inclusively.

s= 'VhexKW4M4vCdVUKqsF45YNsNJ4JitlAdS0UCamptolomacdo7JcJlLkoarbKePLGlcSZFfG27b5q3pX4xVK7pxMqMyHYRefh9wsOuu8ZXYGxTLeJKmCyo0Bjuyunicust3ss7C38OZoHl4DyFsVfWmsJ8q62SW11GMgfhXcdRAv8Fb7cv91nzdUDor1hFQ5E'

a= 35

b=44

c= 122

d= 127

R= s[a:b+1]+' '+ s[c:d+1]

print (R)