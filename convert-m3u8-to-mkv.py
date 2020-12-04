import argparse, sys
from pathlib import Path
import ffmpeg_streaming
from yaspin import yaspin
from yaspin.spinners import Spinners
from codecs import decode

"""
@return: None
"""
def convertStreamToMkv(httpPathToM3U8, outputName) :
	video = ffmpeg_streaming.input(httpPathToM3U8)
	stream = video.stream2file(ffmpeg_streaming.Formats.h264())
	stream.output(outputName)

"""
Core logic for the terminal application
@return: None
"""
def mainApplication() :
	parser=argparse.ArgumentParser()
	parser.add_argument('--input', help='Specifies the input url file stream location that will be targeted.')
	parser.add_argument('--output', help='Specifies the name of a output file from the input source.')
	parser.add_argument('--path', help='Specifies the where the input file resides and the output file will be created.')
	args = parser.parse_args()

	if args.input == None :
		print("Please provide a URL location for the file you are attempting to convert.")
		return
	else :
		inputPath = args.input
		print("Input location: " + inputPath)

	if args.output == None : 
		output = 'output'
	else : 
		output = args.output
		print("Output file name and extension: " + output)

	with yaspin(Spinners.arc, text="Downloading Video") as spnr :
		spnr.write("Beginning Process")
		convertStreamToMkv(inputPath, output)
		spnr.write("Process Completed")
		spnr.ok("Enjoy!")
	
	return

if __name__ == "__main__" :
	mainApplication()
