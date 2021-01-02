import argparse, sys
import ffmpeg_streaming
from yaspin import yaspin
from yaspin.spinners import Spinners
import pathlib

"""
@return: None
"""
def convertStreamToMkv(httpPathToM3U8, outputNameAndPath) :
	video = ffmpeg_streaming.input(httpPathToM3U8)
	stream = video.stream2file(ffmpeg_streaming.Formats.h264())
	stream.output(outputNameAndPath)

"""
Core logic for the terminal application
@return: None
"""
def mainApplication() :
	parser=argparse.ArgumentParser()
	parser.add_argument('--input', help='Specifies the input url file stream location that will be targeted.')
	parser.add_argument('--localFileName', help='Specifies local file name located in the Downloads directory.')
	parser.add_argument('--output', help='Specifies the name of a output file from the input source.', required=True)
	parser.add_argument('--path', help='Specifies the where the input file resides and the output file will be created.')
	
	args = parser.parse_args()

	print('\n')

	if args.input == None :
		print("No URL provided. Depending on local file.")
	else :
		sourceFile = args.input
		print("Input location: " + sourceFile)

	if args.localFileName != None :
		sourceFile = pathlib.Path.home() / 'Downloads' / args.localFileName
		print("Local file name provided. Will continue using the following file: " + str(sourceFile))

	if args.input == None and args.localFileName == None :
		print("Please specify a source file. Remote url and a local file was not provided.")
		print("Exiting program.")
		return

	if args.input != None and args.localFileName != None :
		print("Please only specify one target source to encode.")
		print("Exiting program.")
		return

	if args.output == None : 
		output = 'output'
	else : 
		output = args.output
		print("Output file name and extension: " + output)

	if args.path == None : 
		path = pathlib.Path.home() / 'Downloads'
		print("Path not specified. Defaulting to macOS downloads.")
	else : 
		path = args.path

	fullOutputPathWithFileNameAndExtension = path / output
	print("Creating video at location: " + fullOutputPathWithFileNameAndExtension.as_posix())
	
	print('\n')

	with yaspin(Spinners.arc, text="Downloading Video", color="blue") as spnr :
		convertStreamToMkv(sourceFile, fullOutputPathWithFileNameAndExtension.as_posix())
		spnr.text = "Video Downloaded"
		spnr.ok("Enjoy!")

	return

if __name__ == "__main__" :
	mainApplication()
