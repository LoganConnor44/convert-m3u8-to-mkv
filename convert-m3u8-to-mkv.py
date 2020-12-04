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
	parser.add_argument('--input', help='Specifies the input url file stream location that will be targeted.', required=True)
	parser.add_argument('--output', help='Specifies the name of a output file from the input source.', required=True)
	parser.add_argument('--path', help='Specifies the where the input file resides and the output file will be created.')
	args = parser.parse_args()

	print('\n')

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

	if args.path == None : 
		path = pathlib.Path.home() / 'Downloads'
		print("Path not specified. Defaulting to macOS downloads.")
	else : 
		path = args.path

	fullOutputPathWithFileNameAndExtension = path / output
	print("Creating video at location: " + fullOutputPathWithFileNameAndExtension.as_posix())
	
	print('\n')

	with yaspin(Spinners.arc, text="Downloading Video", color="blue") as spnr :
		convertStreamToMkv(inputPath, fullOutputPathWithFileNameAndExtension.as_posix())
		spnr.text = "Video Downloaded"
		spnr.ok("Enjoy!")

	return

if __name__ == "__main__" :
	mainApplication()
