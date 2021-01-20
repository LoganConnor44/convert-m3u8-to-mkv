import argparse
import pathlib
import ffmpeg_streaming
from yaspin import yaspin
from yaspin.spinners import Spinners

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
	parser.add_argument('--output', help='Specifies the name of a output file from the input source.', required=True)
	parser.add_argument('--path', help='Specifies the where the input file resides and the output file will be created.')
	
	args = parser.parse_args()

	print('\n')

	if args.input == None :
		print("No URL provided.")
		print("Exiting program.")
		return
	else :
		sourceFile = args.input

	if args.output == None : 
		output = 'output'
	else : 
		output = args.output
		print("Output file name and extension: " + output)

	if args.path == None : 
		path = pathlib.Path('/usr/src/app/temp')
	else : 
		path = args.path

	fullOutputPathWithFileNameAndExtension = path / output
	print("Creating video at location: " + fullOutputPathWithFileNameAndExtension.as_posix())
	
	print('\n')

	with yaspin(Spinners.arc, text="Downloading Video", color="blue") as spnr :
		convertStreamToMkv(sourceFile, fullOutputPathWithFileNameAndExtension.as_posix())
		spnr.text = "Video Downloaded To Temporary Location"
		spnr.ok("Enjoy!")
	
	print("Please use the command `docker cp name-of-container:" + fullOutputPathWithFileNameAndExtension.as_posix() + " /host/path/target` to copy the file.")
	print("Once the file is on your host machine, remember to remove the container with the `docker rm container-name-here` command.")
	print("If you are attempting to then copy the file to another filesystem on the network you may use this to enable ssh copy.")
	print("First remember to create a folder that you intend to copy into.")
	print("scp ./new-video-file.mkv account-name@network-location:/media/exfat/media/chinese-videos/new-folder-here/new-video.mkv")
	return

if __name__ == "__main__" :
	mainApplication()
