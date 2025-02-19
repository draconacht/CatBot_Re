import os
import pandas as pd

absol = os.path.dirname(__file__)+"\\"
datax = []
dirx = absol+"\\units"
columns = ['-18- health (x17 for level 30 w/ treasure stat)',
'-14- knockback',
'-10- movement speed',
'-C - attack power (x17 for level 30 w/ treasure stat)',
'-8 - attack recoil (x2) (Attack freq. is foreswing + recoil if less than backswing, then multiplied twice)',
'-4 - attack range',
'0  - cost (EoC 1 costs)',
'4  - recharging time (x2) (-264 after multiplying by 2 for recharge with treasure)',
'8  - Hitbox position (unused)',
'C  - Hitbox size',
'10 - target red',
'14 - ??? (unused)',
'18 - single attack (0), area attack (1)',
'1C - First frame attack',
'20 - Min Layer appearance',
'24 - Max Layer appearance',
'28 - target floating',
'2C - target black',
'30 - target metal',
'34 - target white',
'38 - target angel',
'3C - target alien',
'40 - target zombie',
'44 - strong against',
'48 - knockback (chance rate - %)',
'4C - freeze (chance rate - %)',
'50 - freeze (effect duration)',
'54 - slow (chance rate - %)',
'58 - slow (effect duration)',
'5C - resistant',
'60 - massive damage',
'64 - critical (chance rate - %)',
'68 - attacks only',
'6C - extra money',
'70 - base destroyer',
'74 - wave attack (chance rate - %)',
'78 - wave attack (level)',
'7C - weaken (chance rate - %)',
'80 - weaken (effect duration)',
'84 - weaken (damage reduction, e.g. if set to 25, will weaken enemies to 25% of their attack power)',
'88 - strengthen (health % activation)',
'8C - strengthen (damage increase)',
'90 - survive (chance rate - %)',
'94 - metal attribute',
'98 - long distance (min range)',
'9C - long distance (min range to max range or LD width, negative amount for omnistrike)',
'A0 - resist wave',
'A4 - wave blocker',
'A8 - resist knockback',
'AC - resist freeze',
'B0 - resist slow',
'B4 - resist weaken',
'B8 - zombie killer',
'BC - witch killer',
'C0 - target witch (unused)',
'C4 - Number of attacks before being unable to attack and move, -1 to never do that',
'C8 - Not affected by boss wave',
'CC - Frames before automatically dying, -1 to never die automatically (unused)',
'D0 - 2 to suicide on hit, used in conjunction with C4',
'D4 - First multihit damage',
'D8 - Second multihit damage',
'DC - First multihit frame',
'E0 - Second multihit frame',
'E4 - Use ability (first hit)',
'E8 - Use ability (first multihit)',
'EC - Use ability (second multihit)',
'F0 - Use additional spawn animation, -1 for no spawn animation',
'F4 - Soul anim to use, -1 for no soul at all',
'F8 - Use unique spawn animation',
'FC - Gudetama special soul',
'100 - barrier break',
'104 - Warp chance (unused)',
'108 - Warp duration (unused)',
'10C - Minimum Warp distance (unused)',
'110 - Maximum Warp distance (unused)',
'114 - warp blocker',
'118 - target eva angels (unused)',
'11C - eva angel killer',
'120 - ability affectiveness for relics',
'124 - resist curse',
'128 - Insanely resistant',
'12C - Insanely massive damage',
'130 - Savage blow chance',
'134 - Savage blow damage buff +%',
'138 - Dodge attack chance activation',
'13C - Dodge attack duration',
'140',
'144',
'148',
'14C',
'150',
'154',
'innercounting'
]
for dirs, subdirs, files in os.walk(dirx):
	for f in files:
		if f.endswith('.csv'):
			if not f.endswith('339.csv'):  # fuck iron wall cat
				data2 = pd.read_csv(os.path.join(dirs, f), sep=',', header=None, names=columns, na_filter=False).replace('', 0)
				location = int(f[-7:-4])
				try:
					data2.iat[0, -1] = location * 3
					data2.iat[1, -1] = location * 3 + 1
					data2.iat[2, -1] = location * 3 + 2
				except:
					print(f)
				datax.append(data2.head(3))
frame = pd.concat(datax)
frame.to_csv(absol+'unitsnextgen.csv', sep=',', index=False)
frame['fullswing'] = '0'
print(frame)
for dirs, subdirs, files in os.walk(dirx):
	for f in files:
		if '339' in f:  # fuck iron wall cat
			continue
		if f.endswith('02.maanim') and len(f)<20:
			filename = f[-14:]
			maximum = 0
			with open(dirs+'/'+f, "r", encoding="utf-8") as fp:  # open file, ignore the name
				line = fp.readline()  # get all the lines
				cnt = 1  # need to know which line
				while line:
					if line.count(',') == 3:  # ignore the first lines
						currentvalue = int(line[0:line.find(',')])
						if currentvalue > maximum:
							maximum = currentvalue  # 1st number
					line = fp.readline()
					cnt += 1
			try:
				position = int(filename[:3])
			except ValueError:
				print(filename)
				exit(-1)
			if position > 339:
				position -= 1
			offset = None
			if filename[-10] == 'c':
				offset = 1
			elif filename[-10] == 'f':
				offset = 0
			else:
				offset = 2
			frame.iat[position*3+offset, -1] = maximum+1
frame.to_csv(absol+'unitsnextgen.csv', sep=',', index=False)
# all_csv_files = [file
				 # for path, subdir, files in os.walk(path)
				 # for file in glob(os.path.join(path, EXT))]
# print(all_csv_files)