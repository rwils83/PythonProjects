# Hiding Text in an image

from PIL import Image
import binascii
import optparse

def rgb2hex(r, g, b):
	return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def hex2rgb(hexcode):
	return tuple(map(ord, hexcode[1:].decode('hex')))

def str2bin(message):
	binary = bin(int(binascii.hexlify(message), 16))
	return binary[2:]

def bin2str(binary):
	message = binascii.unhexlify('%x' % (int('0b'+binary,2)))
	return message

def encode(hexcode, digit):
	if hexcode[-1] in ('0','1', '2', '3', '4', '5'):
		hexcode = hexcode[:-1] + digit
		return hexcode
	else:
		return None

def decode(hexcode):
	if hexcode[-1] in ('0', '1'):
		return hexcode[-1]
	else:
		return None

def hide(filename, message):
	img = Image.open(filename)
	binary = str2bin(message) + '1111111111111110'
	if img.mode in ('RGBA'):
		img = img.convert('RGBA')
		datas = img.getdata()
		
		newData = []
		digit = 0
		temp = ''
		for item in datas:
			if (digit < len(binary)):
				newpix = encode(rgb2hex(item[0],item[1],item[2]),binary[digit])
				if newpix == None:
					newData.append(item)
				else:
					r, g, b = hex2rgb(newpix)
					newData.append((r,g,b,255))
					digit += 1
			else:
				newData.append(item)	
		img.putdata(newData)
		img.save(filename, "PNG")
		return "Completed!"
			
	return "Incorrect Image Mode, Couldn't Hide"

						
				

def retr(filename):
	img = Image.open(filename)
	binary = ''
	
	if img.mode in ('RGBA'): 
		img = img.convert('RGBA')
		datas = img.getdata()
		
		for item in datas:
			digit = decode(rgb2hex(item[0],item[1],item[2]))
			if digit == None:
				pass
			else:
				binary = binary + digit
				if (binary[-16:] == '1111111111111110'):
					print "Success"
					return bin2str(binary[:-16])

		return bin2str(binary)
	return "Incorrect Image Mode, Couldn't Retrieve"

def Main():
        parser = optparse.OptionParser('usage %prog '+\
		'-e/-d <target file>')
	parser.add_option('-e', dest='hide', type='string', \
		help='target picture path to hide text')
	parser.add_option('-d', dest='retr', type='string', \
		help='target picture path to retrieve text')
	
	(options, args) = parser.parse_args()
	if (options.hide != None):
		text = raw_input("Enter a message to hide: ")
		print hide(options.hide, text)
	elif (options.retr != None):
                print retr(options.retr)
	else:
		print parser.usage
		exit(0)


if __name__ == '__main__':
	Main()



