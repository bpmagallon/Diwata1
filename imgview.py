import commands

print "Commands:\n"
print "-bin (bin file address) reads bin file"
print "-toa (gain) (exp time(s))convert DN to TOA Radiance"
print "-img (image output filename+img format) converts bin to image file"
print "-att (attitude data address) gives location to image"
print "-footprint (address) creates footprint of image file"
print "\nNote: No space on file address"

print "Enter command: "
command = raw_input()
commands.commRead(command)
