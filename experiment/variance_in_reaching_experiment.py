
import datetime
import viz
import vizinput
import viztask
import vizact
import vizinfo
import vizproximity
import vizshape
import vizfx
import numpy as np
import vizconnect
import csv
import time as time
import os
import errno  # handy system and path functions
import sys  # to get file system encoding


viz.setMultiSample(4)
viz.fov(60)
viz.go()

# dependencies
# "beep.wav"
# "vizcon_localOWL.py" for debugging
# "nvis_complete.py" for lab setup

#Set up the environment
dojo = viz.addChild('pit.osgb')
# flag to indictae debug mode (==1) or lab_setup (==0)
debugging_mode = 0
box_start = vizshape.addBox(size =[0.12,0,0.12], alpha=0,  color=[0.5,0.5,0])

#Add a sensor in the center of the room for the participant to return to after each trial
centerBox = vizshape.addBox(size = [0.5,1.2,0.5], alpha=0.1)
centerBox.setPosition([0,0.5,0])
centerSensor = vizproximity.Sensor(vizproximity.Box([1,1,1]),centerBox)



if debugging_mode == 1:  # true when experiment should be played outside of lab
	vizconnect.go("vizcon_localOWL.py")

	################################################################################################################
	##  get AVATAR
	################################################################################################################
	# import Avatar
	avatar = vizconnect.getAvatar('male')
	#avatar = vizfx.addAvatar("C:\Users\michael\Desktop\_tools_tutorials\Avatars\_twoArms\Cyborg\Cyborg.cfg")

	############################################################################################################
	# Debugging Setup
	############################################################################################################

	#add boxs and create a proximity sensor around each one
	#boxSensors = []

	############################################################################################################
	# Setup for phasespace markers
	############################################################################################################

	# add phasespace node for debugging
	phasespace = viz.add('phasespace.dle',1,'127.0.0.1:2')

	#by viz_config occupied marker have to be called differently to get their positional data
	marker_0 =  vizconnect.getTracker('marker').getNode3d()
	marker_3 =  vizconnect.getTracker('head_0').getNode3d()
	marker_12 = vizconnect.getTracker('marker6').getNode3d()
	marker_14 = vizconnect.getTracker('marker2').getNode3d()
	marker_15 = vizconnect.getTracker('marker3').getNode3d()
	marker_21 = vizconnect.getTracker('marker4').getNode3d()
	marker_22 = vizconnect.getTracker('marker5').getNode3d()

	# add rest of markers
	marker_1 = phasespace.addMarker(1)
	marker_2 = phasespace.addMarker(2)

	marker_4 = phasespace.addMarker(4)
	marker_5 = phasespace.addMarker(5)
	marker_6 = phasespace.addMarker(6)
	marker_7 = phasespace.addMarker(7)
	marker_8 = phasespace.addMarker(8)
	marker_9 = phasespace.addMarker(9)
	marker_10 = phasespace.addMarker(10)
	marker_11 = phasespace.addMarker(11)

	marker_13 = phasespace.addMarker(13)

	marker_16 = phasespace.addMarker(16)
	marker_17 = phasespace.addMarker(17)
	marker_18 = phasespace.addMarker(18)
	marker_19 = phasespace.addMarker(19)
	marker_20 = phasespace.addMarker(20)

	marker_23 = phasespace.addMarker(23)
	marker_24 = phasespace.addMarker(24)
	marker_25 = phasespace.addMarker(25)
	marker_26 = phasespace.addMarker(26)
	marker_27 = phasespace.addMarker(27)
	marker_28 = phasespace.addMarker(28)
	marker_29 = phasespace.addMarker(29)
	marker_30 = phasespace.addMarker(30)
	marker_31 = phasespace.addMarker(31)
	marker_32 = phasespace.addMarker(32)
	marker_33 = phasespace.addMarker(33)
	marker_34 = phasespace.addMarker(34)
	marker_35 = phasespace.addMarker(35)
	marker_36 = phasespace.addMarker(36)
	marker_37 = phasespace.addMarker(37)

	def show_calibration_pos():
		''' function to indicate where subject should be standing during the experiment'''
		print('origin indicated')

		# add red rectangle indicating position
		box_start = vizshape.addBox(size =[0.12,2,0.12], alpha=0.7,  color=[1,0,0])
		# set position of target
		box_start.setPosition([0,1,0])

		# object fades until its no longer visible after 3 secs
		box_start.runAction(vizact.fadeTo(0,time=3))

	# call funtion with "w"
	vizact.onkeydown('w', show_calibration_pos)

	def getpos(subject, csv_):
		''' function to write position (x,y,z) for x markers to csv
			input:
			subject = subject_id
			csv_ = valid csv object
			'''
		#print('marker pos: '+str(marker_0.getPosition()[0]))
		row = '''{time},{marker_0_x},{marker_0_y},{marker_0_z},{marker_1_x},{marker_1_y},{marker_1_z},{marker_2_x},{marker_2_y},{marker_2_z},{marker_3_x},{marker_3_y},{marker_3_z},{marker_4_x},{marker_4_y},{marker_4_z},{marker_5_x},{marker_5_y},{marker_5_z},{marker_6_x},{marker_6_y},{marker_6_z},{marker_7_x},{marker_7_y},{marker_7_z},{marker_8_x},{marker_8_y},{marker_8_z},{marker_9_x},{marker_9_y},{marker_9_z},{marker_10_x},{marker_10_y},{marker_10_z},{marker_11_x},{marker_11_y},{marker_11_z},{marker_12_x},{marker_12_y},{marker_12_z},{marker_13_x},{marker_13_y},{marker_13_z},{marker_14_x},{marker_14_y},{marker_14_z},{marker_15_x},{marker_15_y},{marker_15_z},{marker_16_x},{marker_16_y},{marker_16_z},{marker_17_x},{marker_17_y},{marker_17_z},{marker_18_x},{marker_18_y},{marker_18_z},{marker_19_x},{marker_19_y},{marker_19_z},{marker_20_x},{marker_20_y},{marker_20_z},{marker_21_x},{marker_21_y},{marker_21_z},{marker_22_x},{marker_22_y},{marker_22_z},{marker_23_x},{marker_23_y},{marker_23_z},{marker_24_x},{marker_24_y},{marker_24_z},{marker_25_x},{marker_25_y},{marker_25_z},{marker_26_x},{marker_26_y},{marker_26_z},{marker_27_x},{marker_27_y},{marker_27_z},{marker_28_x},{marker_28_y},{marker_28_z},{marker_29_x},{marker_29_y},{marker_29_z},{marker_30_x},{marker_30_y},{marker_30_z},{marker_31_x},{marker_31_y},{marker_31_z},{marker_32_x},{marker_32_y},{marker_32_z},{marker_33_x},{marker_33_y},{marker_33_z},{marker_34_x},{marker_34_y},{marker_34_z},{marker_35_x},{marker_35_y},{marker_35_z},{marker_36_x},{marker_36_y},{marker_36_z},{marker_37_x},{marker_37_y},{marker_37_z}'''.format(
		time=time.time(),
					marker_0_x=marker_0.getPosition()[0],marker_0_y=marker_0.getPosition()[1], marker_0_z=marker_0.getPosition()[2],
					marker_1_x=marker_1.getPosition()[0],marker_1_y=marker_1.getPosition()[1], marker_1_z=marker_1.getPosition()[2],
					marker_2_x=marker_2.getPosition()[0],marker_2_y=marker_2.getPosition()[1], marker_2_z=marker_2.getPosition()[2],
					marker_3_x=marker_3.getPosition()[0],marker_3_y=marker_3.getPosition()[1], marker_3_z=marker_3.getPosition()[2],
					marker_4_x=marker_4.getPosition()[0],marker_4_y=marker_4.getPosition()[1], marker_4_z=marker_4.getPosition()[2],
					marker_5_x=marker_5.getPosition()[0],marker_5_y=marker_5.getPosition()[1], marker_5_z=marker_5.getPosition()[2],
					marker_6_x=marker_6.getPosition()[0],marker_6_y=marker_6.getPosition()[1], marker_6_z=marker_6.getPosition()[2],
					marker_7_x=marker_7.getPosition()[0],marker_7_y=marker_7.getPosition()[1], marker_7_z=marker_7.getPosition()[2],
					marker_8_x=marker_8.getPosition()[0],marker_8_y=marker_8.getPosition()[1], marker_8_z=marker_8.getPosition()[2],
					marker_9_x=marker_9.getPosition()[0],marker_9_y=marker_9.getPosition()[1], marker_9_z=marker_9.getPosition()[2],
					marker_10_x=marker_10.getPosition()[0], marker_10_y=marker_10.getPosition()[1], marker_10_z=marker_10.getPosition()[2],
					marker_11_x=marker_11.getPosition()[0], marker_11_y=marker_11.getPosition()[1], marker_11_z=marker_11.getPosition()[2],
					marker_12_x=marker_12.getPosition()[0], marker_12_y=marker_12.getPosition()[1], marker_12_z=marker_12.getPosition()[2],
					marker_13_x=marker_13.getPosition()[0], marker_13_y=marker_13.getPosition()[1], marker_13_z=marker_13.getPosition()[2],
					marker_14_x=marker_14.getPosition()[0], marker_14_y=marker_14.getPosition()[1], marker_14_z=marker_14.getPosition()[2],
					marker_15_x=marker_15.getPosition()[0], marker_15_y=marker_15.getPosition()[1], marker_15_z=marker_16.getPosition()[2],
					marker_16_x=marker_16.getPosition()[0], marker_16_y=marker_16.getPosition()[1], marker_16_z=marker_16.getPosition()[2],
					marker_17_x=marker_17.getPosition()[0], marker_17_y=marker_17.getPosition()[1], marker_17_z=marker_17.getPosition()[2],
					marker_18_x=marker_18.getPosition()[0], marker_18_y=marker_18.getPosition()[1], marker_18_z=marker_18.getPosition()[2],
					marker_19_x=marker_19.getPosition()[0], marker_19_y=marker_19.getPosition()[1], marker_19_z=marker_19.getPosition()[2],
					marker_20_x=marker_20.getPosition()[0], marker_20_y=marker_20.getPosition()[1], marker_20_z=marker_20.getPosition()[2],
					marker_21_x=marker_21.getPosition()[0], marker_21_y=marker_21.getPosition()[1], marker_21_z=marker_20.getPosition()[2],
					marker_22_x=marker_22.getPosition()[0], marker_22_y=marker_22.getPosition()[1], marker_22_z=marker_22.getPosition()[2],
					marker_23_x=marker_23.getPosition()[0], marker_23_y=marker_23.getPosition()[1], marker_23_z=marker_23.getPosition()[2],
					marker_24_x=marker_24.getPosition()[0], marker_24_y=marker_24.getPosition()[1], marker_24_z=marker_24.getPosition()[2],
					marker_25_x=marker_25.getPosition()[0], marker_25_y=marker_25.getPosition()[1], marker_25_z=marker_25.getPosition()[2],
					marker_26_x=marker_26.getPosition()[0], marker_26_y=marker_26.getPosition()[1], marker_26_z=marker_26.getPosition()[2],
					marker_27_x=marker_27.getPosition()[0], marker_27_y=marker_27.getPosition()[1], marker_27_z=marker_27.getPosition()[2],
					marker_28_x=marker_28.getPosition()[0], marker_28_y=marker_28.getPosition()[1], marker_28_z=marker_28.getPosition()[2],
					marker_29_x=marker_29.getPosition()[0], marker_29_y=marker_29.getPosition()[1], marker_29_z=marker_29.getPosition()[2],
					marker_30_x=marker_30.getPosition()[0], marker_30_y=marker_30.getPosition()[1], marker_30_z=marker_30.getPosition()[2],
					marker_31_x=marker_31.getPosition()[0], marker_31_y=marker_31.getPosition()[1], marker_31_z=marker_31.getPosition()[2],
					marker_32_x=marker_32.getPosition()[0], marker_32_y=marker_32.getPosition()[1], marker_32_z=marker_32.getPosition()[2],
					marker_33_x=marker_33.getPosition()[0], marker_33_y=marker_33.getPosition()[1], marker_33_z=marker_33.getPosition()[2],
					marker_34_x=marker_34.getPosition()[0], marker_34_y=marker_34.getPosition()[1], marker_34_z=marker_34.getPosition()[2],
					marker_35_x=marker_35.getPosition()[0], marker_35_y=marker_35.getPosition()[1], marker_35_z=marker_35.getPosition()[2],
					marker_36_x=marker_36.getPosition()[0], marker_36_y=marker_36.getPosition()[1], marker_36_z=marker_36.getPosition()[2],
					marker_37_x=marker_37.getPosition()[0], marker_37_y=marker_37.getPosition()[1], marker_37_z=marker_37.getPosition()[2])

		# save results of trial
		row_break = '\n'
		csv_.write(row)
		csv_.write(row_break)



	################################################################################################################
	## Setup event managers and corresponding targets
	################################################################################################################

	# define right hand target marker
	#target_r = vizproximity.Target(marker_r)
	target_r = vizproximity.Target(marker_16)

	# define left hand target marker
	#target_l = vizproximity.Target(marker_l)
	target_l = vizproximity.Target(marker_21)

	#Create proximity manager and set debug on. Toggle debug with d key
	manager_l = vizproximity.Manager()
	manager_l.setDebug(viz.ON)
	debugEventHandle = vizact.onkeydown('d',manager_l.setDebug,viz.TOGGLE)

	# add makrer as target for proximity events
	manager_l.addTarget(target_l)

	#Create proximity manager and set debug on. Toggle debug with d key
	manager_r = vizproximity.Manager()
	manager_r.setDebug(viz.ON)
	debugEventHandle = vizact.onkeydown('d',manager_r.setDebug,viz.TOGGLE)

	# add makrer as target for proximity events
	manager_r.addTarget(target_r)
	#boxSensors = []

elif debugging_mode == 0:  # only applicable in VR-Lab

	vizconnect.go("nvis_complete.py")

	################################################################################################################
	##  get AVATAR
	################################################################################################################
	# import Avatar
	avatar = vizconnect.getAvatar('male')

	def printBone():
		global avatar
		rhand = avatar.getAttachmentPoint('r_hand').getNode3d()
		print rhand.getPosition()

	def show_calibration_pos():
		''' function to indicate where subject should be standing during the experiment'''
		print('origin indicated')

		# add red rectangle indicating position
		box_start = vizshape.addBox(size =[0.12,2,0.12], alpha=0.7,  color=[1,0,0])
		# set position of target
		box_start.setPosition([0,1,0])

		# object fades until its no longer visible after 3 secs
		box_start.runAction(vizact.fadeTo(0,time=3))

	# call funtion with "w"
	vizact.onkeydown('w', show_calibration_pos)



	############################################################################################################
	# Setup for phasespace markers
	############################################################################################################
	#by viz config occupied marker have to be called differentlt to get their positional dara
	#marker =  vizconnect.getTracker('marker').getNode3d()
	#rigid bodies
	#> mark 0,1,2,3 -> head
	# > mark 14,15,16 -> lefthand
	# > mark 21,22,23 -> righthand
	#phasespace = viz.add('phasespace.dle',1,'192.168.1.230')
	vrpn = viz.addExtension('vrpn7.dle')
	VRPN_SOURCE = 'Tracker0@localhost'
	marker_r = vizconnect.getTracker('vrpn3').getNode3d()
	marker_l = vizconnect.getTracker('vrpn2').getNode3d()
	marker_head = vizconnect.getTracker('vrpn').getNode3d()

	#markerggg= vizconnect.getTracker('vrpn4').getNode3d()
	# get marker to log movement data
	marker_0 =  vrpn.addTracker(VRPN_SOURCE,0)
	marker_1 =  vrpn.addTracker(VRPN_SOURCE,1)
	marker_2 =  vrpn.addTracker(VRPN_SOURCE,2)
	marker_3 =  vrpn.addTracker(VRPN_SOURCE,3)
	marker_4 =  vrpn.addTracker(VRPN_SOURCE,4)
	marker_5 =  vrpn.addTracker(VRPN_SOURCE,5)
	marker_6 =  vrpn.addTracker(VRPN_SOURCE,6)
	marker_7 =  vrpn.addTracker(VRPN_SOURCE,7)
	marker_8 =  vrpn.addTracker(VRPN_SOURCE,8)
	marker_9 =  vrpn.addTracker(VRPN_SOURCE,9)
	marker_10 =  vrpn.addTracker(VRPN_SOURCE,10)
	marker_11 =  vrpn.addTracker(VRPN_SOURCE,11)
	marker_12 =  vrpn.addTracker(VRPN_SOURCE,12)
	marker_13 =  vrpn.addTracker(VRPN_SOURCE,13)
	marker_14 =  vrpn.addTracker(VRPN_SOURCE,14)
	marker_15 =  vrpn.addTracker(VRPN_SOURCE,15)
	marker_16 =  vrpn.addTracker(VRPN_SOURCE,16)
	marker_17 =  vrpn.addTracker(VRPN_SOURCE,17)
	marker_18 =  vrpn.addTracker(VRPN_SOURCE,18)
	marker_19 =  vrpn.addTracker(VRPN_SOURCE,19)
	marker_20 =  vrpn.addTracker(VRPN_SOURCE,20)
	marker_21 =  vrpn.addTracker(VRPN_SOURCE,21)
	marker_22 =  vrpn.addTracker(VRPN_SOURCE,22)
	marker_23 =  vrpn.addTracker(VRPN_SOURCE,23)
	marker_24 =  vrpn.addTracker(VRPN_SOURCE,24)
	marker_25 =  vrpn.addTracker(VRPN_SOURCE,25)
	marker_26 =  vrpn.addTracker(VRPN_SOURCE,26)
	marker_27 =  vrpn.addTracker(VRPN_SOURCE,27)
	marker_28 =  vrpn.addTracker(VRPN_SOURCE,28)
	marker_29 =  vrpn.addTracker(VRPN_SOURCE,29)
	marker_30 =  vrpn.addTracker(VRPN_SOURCE,30)
	marker_31 =  vrpn.addTracker(VRPN_SOURCE,31)
	marker_32 =  vrpn.addTracker(VRPN_SOURCE,32)
	marker_33 =  vrpn.addTracker(VRPN_SOURCE,33)
	marker_34 =  vrpn.addTracker(VRPN_SOURCE,34)
	marker_35 =  vrpn.addTracker(VRPN_SOURCE,35)
	marker_36 =  vrpn.addTracker(VRPN_SOURCE,36)
	marker_37 =  vrpn.addTracker(VRPN_SOURCE,37)



	def getpos(subject, csv_):
		''' function to write positional for x markers to csv
			input:
			subject = subject_id
			csv_ = valid csv object
			'''
		#print('marker pos: '+str(marker_0.getPosition()[0]))
		row = '''{time},{marker_0_x},{marker_0_y},{marker_0_z},{marker_1_x},{marker_1_y},{marker_1_z},{marker_2_x},{marker_2_y},{marker_2_z},{marker_3_x},{marker_3_y},{marker_3_z},{marker_4_x},{marker_4_y},{marker_4_z},{marker_5_x},{marker_5_y},{marker_5_z},{marker_6_x},{marker_6_y},{marker_6_z},{marker_7_x},{marker_7_y},{marker_7_z},{marker_8_x},{marker_8_y},{marker_8_z},{marker_9_x},{marker_9_y},{marker_9_z},{marker_10_x},{marker_10_y},{marker_10_z},{marker_11_x},{marker_11_y},{marker_11_z},{marker_12_x},{marker_12_y},{marker_12_z},{marker_13_x},{marker_13_y},{marker_13_z},{marker_14_x},{marker_14_y},{marker_14_z},{marker_15_x},{marker_15_y},{marker_15_z},{marker_16_x},{marker_16_y},{marker_16_z},{marker_17_x},{marker_17_y},{marker_17_z},{marker_18_x},{marker_18_y},{marker_18_z},{marker_19_x},{marker_19_y},{marker_19_z},{marker_20_x},{marker_20_y},{marker_20_z},{marker_21_x},{marker_21_y},{marker_21_z},{marker_22_x},{marker_22_y},{marker_22_z},{marker_23_x},{marker_23_y},{marker_23_z},{marker_24_x},{marker_24_y},{marker_24_z},{marker_25_x},{marker_25_y},{marker_25_z},{marker_26_x},{marker_26_y},{marker_26_z},{marker_27_x},{marker_27_y},{marker_27_z},{marker_28_x},{marker_28_y},{marker_28_z},{marker_29_x},{marker_29_y},{marker_29_z},{marker_30_x},{marker_30_y},{marker_30_z},{marker_31_x},{marker_31_y},{marker_31_z},{marker_32_x},{marker_32_y},{marker_32_z},{marker_33_x},{marker_33_y},{marker_33_z},{marker_34_x},{marker_34_y},{marker_34_z},{marker_35_x},{marker_35_y},{marker_35_z},{marker_36_x},{marker_36_y},{marker_36_z},{marker_37_x},{marker_37_y},{marker_37_z}'''.format(
		time=time.time(),
					marker_0_x=marker_0.getPosition()[0],marker_0_y=marker_0.getPosition()[1], marker_0_z=marker_0.getPosition()[2],
					marker_1_x=marker_1.getPosition()[0],marker_1_y=marker_1.getPosition()[1], marker_1_z=marker_1.getPosition()[2],
					marker_2_x=marker_2.getPosition()[0],marker_2_y=marker_2.getPosition()[1], marker_2_z=marker_2.getPosition()[2],
					marker_3_x=marker_3.getPosition()[0],marker_3_y=marker_3.getPosition()[1], marker_3_z=marker_3.getPosition()[2],
					marker_4_x=marker_4.getPosition()[0],marker_4_y=marker_4.getPosition()[1], marker_4_z=marker_4.getPosition()[2],
					marker_5_x=marker_5.getPosition()[0],marker_5_y=marker_5.getPosition()[1], marker_5_z=marker_5.getPosition()[2],
					marker_6_x=marker_6.getPosition()[0],marker_6_y=marker_6.getPosition()[1], marker_6_z=marker_6.getPosition()[2],
					marker_7_x=marker_7.getPosition()[0],marker_7_y=marker_7.getPosition()[1], marker_7_z=marker_7.getPosition()[2],
					marker_8_x=marker_8.getPosition()[0],marker_8_y=marker_8.getPosition()[1], marker_8_z=marker_8.getPosition()[2],
					marker_9_x=marker_9.getPosition()[0],marker_9_y=marker_9.getPosition()[1], marker_9_z=marker_9.getPosition()[2],
					marker_10_x=marker_10.getPosition()[0], marker_10_y=marker_10.getPosition()[1], marker_10_z=marker_10.getPosition()[2],
					marker_11_x=marker_11.getPosition()[0], marker_11_y=marker_11.getPosition()[1], marker_11_z=marker_11.getPosition()[2],
					marker_12_x=marker_12.getPosition()[0], marker_12_y=marker_12.getPosition()[1], marker_12_z=marker_12.getPosition()[2],
					marker_13_x=marker_13.getPosition()[0], marker_13_y=marker_13.getPosition()[1], marker_13_z=marker_13.getPosition()[2],
					marker_14_x=marker_14.getPosition()[0], marker_14_y=marker_14.getPosition()[1], marker_14_z=marker_14.getPosition()[2],
					marker_15_x=marker_15.getPosition()[0], marker_15_y=marker_15.getPosition()[1], marker_15_z=marker_16.getPosition()[2],
					marker_16_x=marker_16.getPosition()[0], marker_16_y=marker_16.getPosition()[1], marker_16_z=marker_16.getPosition()[2],
					marker_17_x=marker_17.getPosition()[0], marker_17_y=marker_17.getPosition()[1], marker_17_z=marker_17.getPosition()[2],
					marker_18_x=marker_18.getPosition()[0], marker_18_y=marker_18.getPosition()[1], marker_18_z=marker_18.getPosition()[2],
					marker_19_x=marker_19.getPosition()[0], marker_19_y=marker_19.getPosition()[1], marker_19_z=marker_19.getPosition()[2],
					marker_20_x=marker_20.getPosition()[0], marker_20_y=marker_20.getPosition()[1], marker_20_z=marker_20.getPosition()[2],
					marker_21_x=marker_21.getPosition()[0], marker_21_y=marker_21.getPosition()[1], marker_21_z=marker_20.getPosition()[2],
					marker_22_x=marker_22.getPosition()[0], marker_22_y=marker_22.getPosition()[1], marker_22_z=marker_22.getPosition()[2],
					marker_23_x=marker_23.getPosition()[0], marker_23_y=marker_23.getPosition()[1], marker_23_z=marker_23.getPosition()[2],
					marker_24_x=marker_24.getPosition()[0], marker_24_y=marker_24.getPosition()[1], marker_24_z=marker_24.getPosition()[2],
					marker_25_x=marker_25.getPosition()[0], marker_25_y=marker_25.getPosition()[1], marker_25_z=marker_25.getPosition()[2],
					marker_26_x=marker_26.getPosition()[0], marker_26_y=marker_26.getPosition()[1], marker_26_z=marker_26.getPosition()[2],
					marker_27_x=marker_27.getPosition()[0], marker_27_y=marker_27.getPosition()[1], marker_27_z=marker_27.getPosition()[2],
					marker_28_x=marker_28.getPosition()[0], marker_28_y=marker_28.getPosition()[1], marker_28_z=marker_28.getPosition()[2],
					marker_29_x=marker_29.getPosition()[0], marker_29_y=marker_29.getPosition()[1], marker_29_z=marker_29.getPosition()[2],
					marker_30_x=marker_30.getPosition()[0], marker_30_y=marker_30.getPosition()[1], marker_30_z=marker_30.getPosition()[2],
					marker_31_x=marker_31.getPosition()[0], marker_31_y=marker_31.getPosition()[1], marker_31_z=marker_31.getPosition()[2],
					marker_32_x=marker_32.getPosition()[0], marker_32_y=marker_32.getPosition()[1], marker_32_z=marker_32.getPosition()[2],
					marker_33_x=marker_33.getPosition()[0], marker_33_y=marker_33.getPosition()[1], marker_33_z=marker_33.getPosition()[2],
					marker_34_x=marker_34.getPosition()[0], marker_34_y=marker_34.getPosition()[1], marker_34_z=marker_34.getPosition()[2],
					marker_35_x=marker_35.getPosition()[0], marker_35_y=marker_35.getPosition()[1], marker_35_z=marker_35.getPosition()[2],
					marker_36_x=marker_36.getPosition()[0], marker_36_y=marker_36.getPosition()[1], marker_36_z=marker_36.getPosition()[2],
					marker_37_x=marker_37.getPosition()[0], marker_37_y=marker_37.getPosition()[1], marker_37_z=marker_37.getPosition()[2])

		# save results of trial
		row_break = '\n'
		csv_.write(row)
		csv_.write(row_break)

	################################################################################################################
	## Setup event managers and corresponding targets
	################################################################################################################

	# define right hand target marker
	target_r = vizproximity.Target(marker_r)
	#target_r = vizproximity.Target(marker_16)

	# define left hand target marker
	target_l = vizproximity.Target(marker_l)
	#target_l = vizproximity.Target(marker_21)

	#Create proximity manager and set debug on. Toggle debug with d key
	manager_l = vizproximity.Manager()
	manager_l.setDebug(viz.ON)
	debugEventHandle = vizact.onkeydown('d',manager_l.setDebug,viz.TOGGLE)

	# add makrer as target for proximity events
	manager_l.addTarget(target_l)

	#Create proximity manager and set debug on. Toggle debug with d key
	manager_r = vizproximity.Manager()
	manager_r.setDebug(viz.ON)
	debugEventHandle = vizact.onkeydown('d',manager_r.setDebug,viz.TOGGLE)

	# add makrer as target for proximity events
	manager_r.addTarget(target_r)
	#manager_l.addTarget(target_l)


	# sensor for starting trials
#	manager_r.addSensor(centerSensor)
#	manager_l.addSensor(centerSensor)

	#boxSensors = []


################################################################################################################
## Setup dependencies 1H Task
################################################################################################################
# setup experimnet flags ; default is false
entered = False
exited = False

# setup global lists to store results
entered_list = []
exited_list = []
trial_result = []


def Enterbox(e, box, color):
	'''Function to save time at which participant first entered box
	input:
	e = vizproximity.sensor
	box = vizshape object
	color = color which vizshape object should display to indicate that sensor
			has been entered
	'''
	global entered, entered_list

	# color box to green over course of 2 seconds
	box.runAction(vizact.fadeTo(viz.GREEN,time=1.5))



	# only true when target is entered the first time in one trial
	if entered is False:
		entered_time = time.time()  # get timestamp of entry
		entered_list.append(entered_time)  # append timestamp to list
	# set event flag to True, so that following entrances in this trial
	# don't get logged
	entered = True



#fade to white when viewpoint moves away
def Exitbox(e, box):
	'''Function to save time at which participant exited box
	input:
	e = vizproximity.sensor of interest
	box = vizshape object
	'''
	global exited, exited_list
	# fade to white upon exiting
	box.runAction(vizact.fadeTo(viz.WHITE,time=1))

	# only true when target is exited the first time in one trial
	if exited is False:
		exited_time =time.time()
		exited_list.append(exited_time)
	# set event flag to True, so that following exits in this trial
	# don't get logged
	exited = True

##############################################################################
## Learning PHASE 1H
##############################################################################

def learningPhase_1H(subject, height, dominant_hand, reaching_distance, head_height, shoulder_height, hip_height, right_pos, left_pos, middle):
	'''
	One handed learningphase. Presents participant with boxes presented in one
	out of 9 possible positions for every trial.
	Waits for participant to reach into a box to start trial, then displays box
	for 5 further seconds.
	Logs time for entering and exiting box.
	There is a 5 seconds waiting period after each trial, before new box is presented.

	input:
	(both result of the participantInfo function called at the beginnig of the exp)
	subject = subject ID
	height = subject height in meters
	dominant_hand = dominant hand of subject
	reaching_distance = approx. reaching distance of subject
	head_height = approx. head height of subject
	shoulder_height = approx. shoulder_height of subject
	hip_height = approx. hip height of subject
	right_pos = rightmost position for stimuli-box in z-dim
	left_pos = lefttmost position for stimuli-box in z-dim
	middle = 0 = middle position for stimuli-box in z-dim

	'''
	global info, entered, exited, entered_list, exited_list, trial_result, debugging_mode
	print(subject)
	now = datetime.datetime.now()  # get current time stamp to append to filename to avoid overwriting data on retries

	
	entered_list = []
	exited_list = []
	trial_result = []
	
	# open csv for to save movement data to
	csv_ = open('data/'+ 'sub-' + str(subject)+ '/' + 'sub-' + str(subject)+ '-1H-learning-data-' + str(now.strftime("%Y_%m_%d_%H_%M")) + '.csv', 'w')
	# write column headers to csv
	columnTitleRow = "time,marker_0_x,marker_0_y,marker_0_z,marker_1_x,marker_1_y,marker_1_z,marker_2_x,marker_2_y,marker_2_z,marker_3_x,marker_3_y,marker_3_z,marker_4_x,marker_4_y,marker_4_z,marker_5_x,marker_5_y,marker_5_z,marker_6_x,marker_6_y,marker_6_z,marker_7_x,marker_7_y,marker_7_z,marker_8_x,marker_8_y,marker_8_z,marker_9_x,marker_9_y,marker_9_z,marker_10_x,marker_10_y,marker_10_z,marker_11_x,marker_11_y,marker_11_z,marker_12_x,marker_12_y,marker_12_z,marker_13_x,marker_13_y,marker_13_z,marker_14_x,marker_14_y,marker_14_z,marker_15_x,marker_15_y,marker_15_z,marker_16_x,marker_16_y,marker_16_z,marker_17_x,marker_17_y,marker_17_z,marker_18_x,marker_18_y,marker_18_z,marker_19_x,marker_19_y,marker_19_z,marker_20_x,marker_20_y,marker_20_z,marker_21_x,marker_21_y,marker_21_z,marker_22_x,marker_22_y,marker_22_z,marker_23_x,marker_23_y,marker_23_z,marker_24_x,marker_24_y,marker_24_z,marker_25_x,marker_25_y,marker_25_z,marker_26_x,marker_26_y,marker_26_z,marker_27_x,marker_27_y,marker_27_z,marker_28_x,marker_28_y,marker_28_z,marker_29_x,marker_29_y,marker_29_z,marker_30_x,marker_30_y,marker_30_z,marker_31_x,marker_31_y,marker_31_z,marker_32_x,marker_32_y,marker_32_z,marker_33_x,marker_33_y,marker_33_z,marker_34_x,marker_34_y,marker_34_z,marker_35_x,marker_35_y,marker_35_z,marker_36_x,marker_36_y,marker_36_z,marker_37_x,marker_37_y,marker_37_z\n"
	csv_.write(columnTitleRow)

	# open separate csv to save trial results and events
	csv = open('data/'+ 'sub-' + str(subject)+ '/' + 'sub-' + str(subject)+ '-1H-learning-events-' + str(now.strftime("%Y_%m_%d_%H_%M")) + '.csv', 'w')
	# write column headers to csv
	columnTitleRow = "trial_start,box_size_id,box_pos_x,box_pos_y,box_pos_z,box_pos_id,result,entered,exited\n"
	csv.write(columnTitleRow)

	# generate array of position identities, which will be called later on
	# might have to be changed to an explicit randomization procedure to balance trials
	arr_position = []
	arr = np.arange(9)
	arr = list(arr)
	# # range of trials
	trials = range(2)
	for j in trials:
		block = np.random.permutation(arr)
		for i in block:
			arr_position.append(block[i])

	size = [0.2,0.2,0.2]
	size_id = 's2'
	size_offset = 0
	# specify default pos of target cube
	pos = [0,0,0]

	# call 'getpos' function every 0.01 sec to log movement data
	postimer = vizact.ontimer(0.01666666666666666666666666666667, getpos, subject, csv_)
	
	# iterate over range of trials
	for i in range(len(arr_position)):
		#print(len(arr_position))
		# set event flags to false
		entered = False
		exited = False

		if debugging_mode == 1:  # print a warning message when debugging mode is true
			print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DEBUGGING MODE ACTIVE : DATA WILL NOT BE SAVED  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

		# waiting period before next box is presented
		yield viztask.waitTime(1)
		# Update Instrcution
		info.setText('Learningphase: Reach for the box')

		# display boxes in possible configurations of a 9x9 grid
		# boxes at approx. head height
		if arr_position[i] == 0:
			pos = [reaching_distance + size_offset, head_height, right_pos]
			pos_id = 'r1'
		elif arr_position[i] == 1:
			pos = [reaching_distance + size_offset, head_height, middle]
			pos_id = 'm1'
		elif arr_position[i] == 2:
			pos = [reaching_distance + size_offset, head_height, left_pos]
			pos_id = 'l1'

		# boxes at approx. chest height
		if arr_position[i] == 3:
			pos = [reaching_distance + size_offset, shoulder_height, right_pos]
			pos_id = 'r2'
		elif arr_position[i] == 4:
			pos = [reaching_distance + size_offset, shoulder_height, middle]
			pos_id = 'm2'
		elif arr_position[i] == 5:
			pos = [reaching_distance + size_offset, shoulder_height, left_pos]
			pos_id = 'l2'

		# boxes at approx. hip height
		elif arr_position[i] == 6:
			pos = [reaching_distance + size_offset, hip_height, right_pos]
			pos_id = 'r3'
		elif arr_position[i] == 7:
			pos = [reaching_distance + size_offset, hip_height, middle]
			pos_id = 'm3'
		elif arr_position[i] == 8:
			pos = [reaching_distance + size_offset, hip_height, left_pos]
			pos_id = 'l3'
		print(pos_id)
		# setup start box
		if dominant_hand == 'l':
			while centerSensor not in manager_l.getActiveSensors():
				yield vizproximity.waitEnter(centerSensor)
		elif dominant_hand == 'r':
			while centerSensor not in manager_r.getActiveSensors():
				yield vizproximity.waitEnter(centerSensor)
		viz.playSound('beep.wav')
		#store the time at which movement started
		startTime = time.time()
		print('started at: '+str(startTime))

		# add target
		box = vizshape.addBox(size = size, alpha=0.5)
		# set position of target
		box.setPosition(pos)
		# define a proximity sensor around target
		sensor = vizproximity.addBoundingBoxSensor(box,  scale=(1,1,1))
		#boxSensors.append(sensor)
		#print(boxSensors)

		# get manager for dominant hand
		if dominant_hand == 'r':
			manager_r.addSensor(sensor)

			# setup functions to log when participant entered and exited target cube
			manager_r.onEnter(sensor, Enterbox, box, viz.RED)
			manager_r.onExit(sensor, Exitbox, box)
		elif dominant_hand == 'l':
			print "magische Stelle"
			manager_l.addSensor(sensor)

			# setup functions to log when participant entered and exited target cube
			manager_l.onEnter(sensor, Enterbox, box, viz.RED)
			manager_l.onExit(sensor, Exitbox, box)
		#Get sensor for this trial
		#sensor = boxSensors[i]

		if debugging_mode == 0:  # only applicable in VR-Lab
		# don't wait for particpant response when debugging

			# wait for participant to enter sensor
			yield vizproximity.waitEnter(sensor)
			viz.playSound('beep.wav')

		# display target cube for 5 seconds after sensor has been entered
		yield viztask.waitTime(3)

		# remove box
		box.remove()
		box_removed = time.time()

		if debugging_mode == 0:  # only applicable in VR-Lab
			try:
				# check if box not exited
				print(exited_list[i])
			except IndexError:
				# append time that box was removed as endpoint if box not exited
				exited_list.append(box_removed)
				print('box_removed')

			#print('entered: ', entered_list)
			#print('exited: ', exited_list) 

			# if hand was kept in cube for less than 2 sec = Failure
			if (exited_list[i] - entered_list[i]) < 1.5:
				info.setText("Failure")
				trial_result.append('failure')

			elif (exited_list[i] - entered_list[i]) >= 1.5:
				info.setText("success")
				trial_result.append('success')

			# save results of trial
			row = (str(startTime) + "," +
					str(size_id) + ',' +
					str(pos[0]) + ',' +
					str(pos[1]) + ',' +
					str(pos[2]) + ',' +
					str(pos_id)+ ',' +
					trial_result[i] + "," +
					str(entered_list[i]) + "," +
					str(exited_list[i]) + "\n")
			yield csv.write(row)


		# check which trial we are in
		print('Trial num: ', str(i))


	#save results
	info.setText('Thank You. You have completed this learning-phase')
	postimer.setEnabled(viz.OFF)
#	print(entered_list)
#	print(exited_list)
#	print(trial_result)

################################################################################################################
## TEST PHASE 1H
################################################################################################################

def testPhase_1H(subject, height, dominant_hand, reaching_distance, head_height, shoulder_height, hip_height, right_pos, left_pos, middle):
	'''
	One handed testphase. Presents participant with boxes presented in one
	out of 9 possible positions for every trial.
	Waits for participant to reach into a box to start trial, then displays box
	for 5 further seconds.
	Logs time for entering and exiting box.
	There is a 5 seconds waiting period after each trial, before new box is presented,
	dedicated break after 2 Blocks, which can be skipped by pressing spacebar.

	input:
	(both result of the participantInfo function called at the beginnig of the exp)
	subject = subject ID
	height = subject height in meters
	dominant_hand = dominant hand of subject
	reaching_distance = approx. reaching distance of subject
	head_height = approx. head height of subject
	shoulder_height = approx. shoulder_height of subject
	hip_height = approx. hip height of subject
	right_pos = rightmost position for stimuli-box in z-dim
	left_pos = lefttmost position for stimuli-box in z-dim
	middle = 0 = middle position for stimuli-box in z-dim
	'''

	global info, entered, exited, entered_list, exited_list, trial_result, debugging_mode
	print(subject)
	now = datetime.datetime.now()  # get current time stamp to append to filename to avoid overwriting data on retries
	
	entered_list = []
	exited_list = []
	trial_result = []

	# open csv to save movement data to
	csv_ = open('data/'+ 'sub-' + str(subject)+ '/' + 'sub-' + str(subject)+ '-1H-data-' + str(now.strftime("%Y_%m_%d_%H_%M")) + '.csv', 'w')
	# write column headers to csv
	columnTitleRow = "time,marker_0_x,marker_0_y,marker_0_z,marker_1_x,marker_1_y,marker_1_z,marker_2_x,marker_2_y,marker_2_z,marker_3_x,marker_3_y,marker_3_z,marker_4_x,marker_4_y,marker_4_z,marker_5_x,marker_5_y,marker_5_z,marker_6_x,marker_6_y,marker_6_z,marker_7_x,marker_7_y,marker_7_z,marker_8_x,marker_8_y,marker_8_z,marker_9_x,marker_9_y,marker_9_z,marker_10_x,marker_10_y,marker_10_z,marker_11_x,marker_11_y,marker_11_z,marker_12_x,marker_12_y,marker_12_z,marker_13_x,marker_13_y,marker_13_z,marker_14_x,marker_14_y,marker_14_z,marker_15_x,marker_15_y,marker_15_z,marker_16_x,marker_16_y,marker_16_z,marker_17_x,marker_17_y,marker_17_z,marker_18_x,marker_18_y,marker_18_z,marker_19_x,marker_19_y,marker_19_z,marker_20_x,marker_20_y,marker_20_z,marker_21_x,marker_21_y,marker_21_z,marker_22_x,marker_22_y,marker_22_z,marker_23_x,marker_23_y,marker_23_z,marker_24_x,marker_24_y,marker_24_z,marker_25_x,marker_25_y,marker_25_z,marker_26_x,marker_26_y,marker_26_z,marker_27_x,marker_27_y,marker_27_z,marker_28_x,marker_28_y,marker_28_z,marker_29_x,marker_29_y,marker_29_z,marker_30_x,marker_30_y,marker_30_z,marker_31_x,marker_31_y,marker_31_z,marker_32_x,marker_32_y,marker_32_z,marker_33_x,marker_33_y,marker_33_z,marker_34_x,marker_34_y,marker_34_z,marker_35_x,marker_35_y,marker_35_z,marker_36_x,marker_36_y,marker_36_z,marker_37_x,marker_37_y,marker_37_z\n"
	csv_.write(columnTitleRow)

	# open separate csv to save trial results and events
	csv = open('data/'+ 'sub-' + str(subject)+ '/' + 'sub-' + str(subject)+ '-1H-events-' + str(now.strftime("%Y_%m_%d_%H_%M")) + '.csv', 'w')
	# write column headers to csv
	columnTitleRow = "trial_start,box_size_id,box_pos_x,box_pos_y,box_pos_z,box_pos_id,result,entered,exited\n"

	csv.write(columnTitleRow)

	# generate array of position identities, which will be called later on
	arr_position = []
	arr = np.arange(9)
	arr = list(arr)
	# range of trials
	trials = range(20)
	# permutate trials into 20 complete Blocks
	for j in trials:
		block = np.random.permutation(arr)
		for i in block:
			arr_position.append(block[i])

	# specify default pos and size of target cube
	pos = [0,0,0]
	size = [0.20,0.20,0.20]
	size_id = 's2'
	size_offset = 0
	# call 'getpos' function every 0.016 sec (60hz) to log movement data
	#vizact.ontimer(0.01666666666666666666666666666667, getpos, subject, csv_)
	postimer = vizact.ontimer(0.01666666666666666666666666666667, getpos, subject, csv_)

	# iterate over blocks of trials
	for i in range(len(arr_position)):
		# set event flags to false
		entered = False
		exited = False

		if debugging_mode == 1:  # print a warning message when debugging mode is true
			print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DEBUGGING MODE ACTIVE : DATA WILL NOT BE SAVED  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

		# waiting period before next box is presented
		yield viztask.waitTime(1)

		# Update Instrcution
		info.setText('Testphase: Reach for the box')

		# display boxes in possible configurations of a 9x9 grid
		# boxes at approx. head height
		if arr_position[i] == 0:
			pos = [reaching_distance + size_offset, head_height, right_pos]
			pos_id = 'r1'
		elif arr_position[i] == 1:
			pos = [reaching_distance + size_offset, head_height, middle]
			pos_id = 'm1'
		elif arr_position[i] == 2:
			pos = [reaching_distance + size_offset, head_height, left_pos]
			pos_id = 'l1'

		# boxes at approx. chest height
		if arr_position[i] == 3:
			pos = [reaching_distance + size_offset, shoulder_height, right_pos]
			pos_id = 'r2'
		elif arr_position[i] == 4:
			pos = [reaching_distance + size_offset, shoulder_height, middle]
			pos_id = 'm2'
		elif arr_position[i] == 5:
			pos = [reaching_distance + size_offset, shoulder_height, left_pos]
			pos_id = 'l2'

		# boxes at approx. hip height
		elif arr_position[i] == 6:
			pos = [reaching_distance + size_offset, hip_height, right_pos]
			pos_id = 'r3'
		elif arr_position[i] == 7:
			pos = [reaching_distance + size_offset, hip_height, middle]
			pos_id = 'm3'
		elif arr_position[i] == 8:
			pos = [reaching_distance + size_offset, hip_height, left_pos]
			pos_id = 'l3'
		print(pos_id)
		manager_r.addSensor(centerSensor)
		# setup target box
		while centerSensor not in manager_r.getActiveSensors():
			yield vizproximity.waitEnter(centerSensor)
		viz.playSound('beep.wav')
		#store the time at which movement started
		startTime = time.time()
		print('started at: '+str(startTime))

		# setup target box
		box = vizshape.addBox(size = size, alpha=0.5)
		# set position of target
		box.setPosition(pos)
		# define a proximity sensor around target
		sensor = vizproximity.addBoundingBoxSensor(box,  scale=(1,1,1))
		#boxSensors.append(sensor)

		# get manager for dominant hand
		if dominant_hand == 'r':
			manager_r.addSensor(sensor)

			# setup functions to log when participant entered and exited target cube
			manager_r.onEnter(sensor, Enterbox, box, viz.RED)
			manager_r.onExit(sensor, Exitbox, box)
		elif dominant_hand == 'l':
			manager_l.addSensor(sensor)

			# setup functions to log when participant entered and exited target cube
			manager_l.onEnter(sensor, Enterbox, box, viz.RED)
			manager_l.onExit(sensor, Exitbox, box)
		#Get sensor for this trial
		#sensor = boxSensors[i]

		if debugging_mode == 0:  # only applicable in VR-Lab
			# wait for participant to enter sensor
			if dominant_hand == 'r':
				assert(sensor in manager_r.getSensors()),"Nicht drin. Manager enthält: {}".format(manager_r.getSensors())
			elif dominant_hand == 'l':
				assert(sensor in manager_l.getSensors()),"Nicht drin. Manager enthält: {}".format(manager_l.getSensors())
			yield vizproximity.waitEnter(sensor)
			viz.playSound('beep.wav')

		# display target cube for 5 seconds after sensor has been entered
		yield viztask.waitTime(3)
		
		# remove box
		box.remove()
		box_removed = time.time()

		if debugging_mode == 0:  # only applicable in VR-Lab
			try:
				# check if box not exited
				print(exited_list[i])
			except IndexError:
				# append time that box was removed as endpoint if box not exited
				exited_list.append(box_removed)
				print('box_removed')

			#print('entered: ', entered_list)
			#print('exited: ', exited_list)

			# if hand was kept in cube for less than 2 sec = Failure
			if (exited_list[i] - entered_list[i]) < 1.5:
				info.setText("Failure")
				trial_result.append('failure')

			elif (exited_list[i] - entered_list[i]) >= 1.5:
				info.setText("success")
				trial_result.append('success')

			# save results of trial
			row = (str(startTime) + "," +
					str(size_id) + ',' +
					str(pos[0]) + ',' +
					str(pos[1]) + ',' +
					str(pos[2]) + ',' +
					str(pos_id)+ ',' +
					trial_result[i] + "," +
					str(entered_list[i]) + "," +
					str(exited_list[i]) + "\n")
			csv.write(row)

		# check which trial we are in
		print('Trial num: ', str(i))
		# break after 18 trials
		if ((i-1) % 18) == 0 and i > 1:
			info.setText('Break')
			# wait for button press to continue experiment
			yield viztask.waitKeyDown(' ')


	#save results
	info.setText('Thank You. You have completed the first phase')
	postimer.setEnabled(viz.OFF)
	print(entered_list)
	print(exited_list)
	print(trial_result)


################################################################################################################
## Setup dependencies 2H Task
################################################################################################################
# setup experimnet flags
entered_r = False
exited_r = False

entered_l = False
exited_l = False

# setup global lists to store results
entered_list_r = []
exited_list_r = []
trial_result_r = []

entered_list_l = []
exited_list_l = []
trial_result_l = []

#fade to true color when viewpoint moves near
def Enterbox_r(e, box, color):
	'''Function to save time at which participant first entered left hand box
	input:
	e = vizproximity.sensor of interest
	box = vizshape object
	color = color which vizshape object should display to indicate that sensor
			has been entered
	'''
	global entered_r, entered_list_r

	#Create an action to fade out for 2 seconds
	box.runAction(vizact.fadeTo(viz.GREEN,time=1.5))

	# only true when target is entered the first time in one trial
	if entered_r is False:
		entered_time = time.time()  # get timestamp of entry
		entered_list_r.append(entered_time)  # append timestamp to list
	# set event flag to True, so that following entrances in this trial
	# don't get logged
	entered_r = True



def Exitbox_r(e, box):
	'''Function to save time at which participant exited box right hand box
	input:
	e = vizproximity.sensor of interest
	box = vizshape object
	'''
	global exited_r, exited_list_r
	# fade to white upon exiting
	box.runAction(vizact.fadeTo(viz.WHITE,time=1))

	# only true when target is exited the first time in one trial
	if exited_r is False:
		exited_time =time.time()
		exited_list_r.append(exited_time)
	# set event flag to True, so that following exits in this trial
	# don't get logged
	exited_r = True

#fade to true color when viewpoint moves near
def Enterbox_l(e, box, color):
	'''Function to save time at which participant first entered left hand box
	input:
	e = vizproximity.sensor of interest
	box = vizshape object
	color = color which vizshape object should display to indicate that sensor
			has been entered
	'''
	global entered_l, entered_list

	#Create an action to fade out for 2 seconds
	box.runAction(vizact.fadeTo(viz.GREEN,time=2))

	# only true when target is entered the first time in one trial
	if entered_l is False:
		entered_time = time.time()  # get timestamp of entry
		entered_list_l.append(entered_time)  # append timestamp to list
	# set event flag to True, so that following entrances in this trial
	# don't get logged
	entered_l = True

def Exitbox_l(e, box):
	'''Function to save time at which participant exited box left hand box
	input:
	e = vizproximity.sensor of interest
	box = vizshape object
	'''
	global exited_l, exited_list_l
	# fade to white upon exiting
	box.runAction(vizact.fadeTo(viz.WHITE,time=1))

	# only true when target is exited the first time in one trial
	if exited_l is False:
		exited_time =time.time()
		exited_list_l.append(exited_time)
	# set event flag to True, so that following exits in this trial
	# don't get logged
	exited_l = True

def getEnter_r():
	global entered_l, exited_l, entered_r, exited_r

	return entered_r

def getEnter_l():
	global entered_l, exited_l, entered_r, exited_r

	return entered_l
################################################################################################################
## Learning PHASE 2H
################################################################################################################


def learningPhase_2H_position_difference(subject, height, dominant_hand, reaching_distance, head_height, shoulder_height, hip_height, right_pos, left_pos, middle):
	'''
	Two handed testphase. Presents participant with 2 boxes presented in one
	out of 9 possible positions each for every trial.
	Waits for participant to reach into a box to start trial, then displays box
	for 5 further seconds.
	Logs time for entering and exiting box.
	There is a 5 seconds waiting period after each trial, before new boxes are presented.

	input:
	(both result of the participantInfo function called at the beginnig of the exp)
	subject = subject ID
	height = subject height in meters
	dominant_hand = dominant hand of subject
	reaching_distance = approx. reaching distance of subject
	head_height = approx. head height of subject
	shoulder_height = approx. shoulder_height of subject
	hip_height = approx. hip height of subject
	right_pos = rightmost position for stimuli-box in z-dim
	left_pos = lefttmost position for stimuli-box in z-dim
	middle = 0 = middle position for stimuli-box in z-dim
	'''

	global info, entered_l, exited_l, entered_r, exited_r, entered_list_r, exited_list_r, trial_result_r, entered_list_l, exited_list_l, trial_result_l, debugging_mode
	now = datetime.datetime.now()  # get current time stamp to append to filename to avoid overwriting data on retries
	
	entered_list_r = []
	exited_list_r = []
	trial_result_r = []

	entered_list_l = []
	exited_list_l = []
	trial_result_l = []
	
	# open csv for to save movement data to
	csv_ = open('data/'+ 'sub-' + str(subject)+ '/' + 'sub-' + str(subject)+ '-2H-learning-data-' + str(now.strftime("%Y_%m_%d_%H_%M")) + '.csv', 'w')
	# write column headers to csv
	columnTitleRow = "time,marker_0_x,marker_0_y,marker_0_z,marker_1_x,marker_1_y,marker_1_z,marker_2_x,marker_2_y,marker_2_z,marker_3_x,marker_3_y,marker_3_z,marker_4_x,marker_4_y,marker_4_z,marker_5_x,marker_5_y,marker_5_z,marker_6_x,marker_6_y,marker_6_z,marker_7_x,marker_7_y,marker_7_z,marker_8_x,marker_8_y,marker_8_z,marker_9_x,marker_9_y,marker_9_z,marker_10_x,marker_10_y,marker_10_z,marker_11_x,marker_11_y,marker_11_z,marker_12_x,marker_12_y,marker_12_z,marker_13_x,marker_13_y,marker_13_z,marker_14_x,marker_14_y,marker_14_z,marker_15_x,marker_15_y,marker_15_z,marker_16_x,marker_16_y,marker_16_z,marker_17_x,marker_17_y,marker_17_z,marker_18_x,marker_18_y,marker_18_z,marker_19_x,marker_19_y,marker_19_z,marker_20_x,marker_20_y,marker_20_z,marker_21_x,marker_21_y,marker_21_z,marker_22_x,marker_22_y,marker_22_z,marker_23_x,marker_23_y,marker_23_z,marker_24_x,marker_24_y,marker_24_z,marker_25_x,marker_25_y,marker_25_z,marker_26_x,marker_26_y,marker_26_z,marker_27_x,marker_27_y,marker_27_z,marker_28_x,marker_28_y,marker_28_z,marker_29_x,marker_29_y,marker_29_z,marker_30_x,marker_30_y,marker_30_z,marker_31_x,marker_31_y,marker_31_z,marker_32_x,marker_32_y,marker_32_z,marker_33_x,marker_33_y,marker_33_z,marker_34_x,marker_34_y,marker_34_z,marker_35_x,marker_35_y,marker_35_z,marker_36_x,marker_36_y,marker_36_z,marker_37_x,marker_37_y,marker_37_z\n"
	csv_.write(columnTitleRow)

	# open csv to save trial results and events for each hand
	csv = open('data/'+ 'sub-' + str(subject)+ '/' + 'sub-' + str(subject)+ '-2H-learning-events-' + str(now.strftime("%Y_%m_%d_%H_%M")) + '.csv', 'w')
	# write column headers to csv
	columnTitleRow = "trial_start,box_size_id,box_pos_id,box_r_pos_x,box_r_pos_y,box_r_pos_z,box_pos_id_r,result_r,entered_r,exited_r,box_l_pos_x,box_l_pos_y,box_l_pos_z,box_pos_id_l,result_l,entered_l,exited_l\n"

	csv.write(columnTitleRow)

	# generate array of position identities, which will be called later on
	# might have to be changed to an explicit randomization procedure to balance trials
	arr_position = []
	arr = np.arange(13)
	arr = list(arr)
	# # range of trials
	trials = range(2)
	for j in trials:
		block = np.random.permutation(arr)
		for i in block:
			arr_position.append(block[i])

	# specify default pos and size of target cube
	pos = [0,0,0]
	size = [0.20,0.20,0.20]
	size_id = 's2'
	size_offset = 0
	# call 'getpos' function every 0.1 sec to log movement data
	#vizact.ontimer(0.01666666666666666666666666666667, getpos, subject, csv_)
	postimer = vizact.ontimer(0.01666666666666666666666666666667, getpos, subject, csv_)
	# define counter to keep track of sensors later on
	counter = 0

	# iterate over range of trials
	for i in range(len(arr_position)):
		# set event flags to false
		entered_r = False
		exited_r = False

		entered_l = False
		exited_l = False

		if debugging_mode == 1:  # print a warning message when debugging mode is true
			print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DEBUGGING MODE ACTIVE : DATA WILL NOT BE SAVED  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

		# waiting period before next box is presented
		yield viztask.waitTime(1)
		# Update Instrcution
		info.setText('Learningphase: Reach for the boxes')

		# boxes at approx. head height
		if arr_position[i] == 0:
			pos_r_box  = [reaching_distance + size_offset, head_height, right_pos]
			pos_l_box  = [reaching_distance + size_offset, head_height, left_pos]
			pos_id_r = 'r1'
			pos_id_l = 'l1'
			pos_id = 'r1-l1'
		elif arr_position[i] == 1:
			pos_r_box  = [reaching_distance + size_offset, head_height, middle]
			pos_l_box  = [reaching_distance + size_offset, head_height, left_pos]
			pos_id_r = 'm1'
			pos_id_l = 'l1'
			pos_id = 'm1-l1'
		elif arr_position[i] == 2:
			pos_r_box  = [reaching_distance + size_offset, head_height, right_pos]
			pos_l_box  = [reaching_distance + size_offset, head_height, middle]
			pos_id_r = 'r1'
			pos_id_l = 'm1'
			pos_id = 'r1-m1'

		# boxes at approx. chest height
		elif arr_position[i] == 3:
			pos_r_box  = [reaching_distance + size_offset,shoulder_height , right_pos]
			pos_l_box  = [reaching_distance + size_offset, shoulder_height, left_pos]
			pos_id_r = 'r2'
			pos_id_l = 'l2'
			pos_id = 'r2-l2'
		elif arr_position[i] == 4:
			pos_r_box  = [reaching_distance + size_offset, shoulder_height, middle]
			pos_l_box  = [reaching_distance + size_offset, shoulder_height, left_pos]
			pos_id_r = 'm2'
			pos_id_l = 'l2'
			pos_id = 'm2-l2'
		elif arr_position[i] == 5:
			pos_r_box  = [reaching_distance + size_offset, shoulder_height, right_pos]
			pos_l_box  = [reaching_distance + size_offset, shoulder_height, middle]
			pos_id_r = 'r2'
			pos_id_l = 'm2'
			pos_id = 'r2-m2'

		# boxes at approx. hip height
		elif arr_position[i] == 6:
			pos_r_box  = [reaching_distance + size_offset, hip_height, right_pos]
			pos_l_box  = [reaching_distance + size_offset, hip_height, left_pos]
			pos_id_r = 'r3'
			pos_id_l = 'l3'
			pos_id = 'r3-l3'
		elif arr_position[i] == 7:
			pos_r_box  = [reaching_distance + size_offset, hip_height, middle]
			pos_l_box  = [reaching_distance + size_offset, hip_height, left_pos]
			pos_id_r = 'm3'
			pos_id_l = 'l3'
			pos_id = 'm3-l3'
		elif arr_position[i] == 8:
			pos_r_box  = [reaching_distance + size_offset, hip_height, right_pos]
			pos_l_box  = [reaching_distance + size_offset, hip_height, middle]
			pos_id_r = 'r3'
			pos_id_l = 'm3'
			pos_id = 'r3-m3'

		# boxes at mixed heights
		elif arr_position[i] == 9:
			pos_r_box  = [reaching_distance + size_offset, head_height, right_pos]
			pos_l_box  = [reaching_distance + size_offset, hip_height, left_pos]
			pos_id_r = 'r1'
			pos_id_l = 'l3'
			pos_id = 'r1-l3'
		elif arr_position[i] == 10:
			pos_r_box  = [reaching_distance + size_offset, hip_height, right_pos]
			pos_l_box  = [reaching_distance + size_offset, head_height, left_pos]
			pos_id_r = 'r3'
			pos_id_l = 'l1'
			pos_id = 'r3-l1'
		elif arr_position[i] == 11:
			pos_r_box  = [reaching_distance + size_offset, head_height, middle]
			pos_l_box  = [reaching_distance + size_offset, hip_height, middle]
			pos_id_r = 'm1'
			pos_id_l = 'm3'
			pos_id = 'm1-m3'
		elif arr_position[i] == 12:
			pos_r_box  = [reaching_distance + size_offset, hip_height, middle]
			pos_l_box  = [reaching_distance + size_offset, head_height, middle]
			pos_id_r = 'm3'
			pos_id_l = 'm1'
			pos_id = 'm3-m1'

#		# setup start  box
#		while centerSensor not in manager_r.getActiveSensors():
#			yield vizproximity.waitEnter(centerSensor)
#		viz.playSound('beep.wav')
		if dominant_hand == 'l':
			while centerSensor not in manager_l.getActiveSensors():
				yield vizproximity.waitEnter(centerSensor)
		elif dominant_hand == 'r':
			while centerSensor not in manager_r.getActiveSensors():
				yield vizproximity.waitEnter(centerSensor)
		viz.playSound('beep.wav')
		#store the time at which movement started
		startTime = time.time()
		print('started at: '+str(startTime))

		print(pos_id_r)
		print(pos_id_l)
		# setup target box
		box_r = vizshape.addBox(size = size, alpha=0.5, color=[0.5,0.5,0])
		# set position of target
		box_r.setPosition(pos_r_box)

		# define a proximity sensor around target
		sensor_r = vizproximity.addBoundingBoxSensor(box_r,  scale=(1,1,1))
		#boxSensors.append(sensor_r)
		manager_r.addSensor(sensor_r)

		# setup target box
		box_l = vizshape.addBox(size = size, alpha=0.5,  color=[0,0,1])
		box_l.setPosition(pos_l_box)
		#print('pos_right' + str(pos_r_box))
		#print('pos_left' + str(pos_l_box))

		# define a proximity sensor around target
		sensor_l= vizproximity.addBoundingBoxSensor(box_l,  scale=(1,1,1))
		#boxSensors.append(sensor_l)
		manager_l.addSensor(sensor_l)

		# setup functions to log when participant entered and exited target boxes
		manager_r.onEnter(sensor_r, Enterbox_r, box_r, viz.RED)
		manager_r.onExit(sensor_r, Exitbox_r, box_r)

		manager_l.onEnter(sensor_l, Enterbox_l, box_l, viz.RED)
		manager_l.onExit(sensor_l, Exitbox_l, box_l)

		#Get sensors for this trial
		#sensor_r = boxSensors[counter]
		#sensor_l = boxSensors[counter+1]

		if debugging_mode == 0:  # only applicable in VR-Lab
			# wait for participant to enter one of the sensors
			con_r = viztask.waitTrue(getEnter_r)
			con_l = viztask.waitTrue(getEnter_l)
			d = yield viztask.waitAll([con_r, con_l])
			#print "Hi"
			viz.playSound('beep.wav')


		# display target cube for 5 seconds after sensor has been entered
		yield viztask.waitTime(3)

		# remove right hand box
		box_r.remove()
		box_removed_r = time.time()
		# left hand
		box_l.remove()
		box_removed_l = time.time()

		if debugging_mode == 0:  # only applicable in VR-Lab
			try:
				# check if right hand box not exited
				print(exited_list_r[i])
			except IndexError:
				# append time that box was removed as endpoint if box not exited
				exited_list_r.append(box_removed_r)
				print('box_removed')
				
			try:
				# check if right hand box not exited
				print(exited_list_l[i])
			except IndexError:
				# append time that box was removed as endpoint if box not exited
				exited_list_l.append(box_removed_l)
				print('box_removed')

			#print('entered: ', entered_list_r)
			#print('exited: ', exited_list_r)

			# if hand was kept in cube for less than 2 sec = Failure
			if (exited_list_r[i] - entered_list_r[i]) < 1.5:
				r_result_info = "Right Hand Failure"
				info.setText(r_result_info)
				trial_result_r.append('failure')

			elif (exited_list_r[i] - entered_list_r[i]) >= 1.5:
				r_result_info = "Right Hand Success"
				info.setText(r_result_info)
				trial_result_r.append('success')


			# if hand was kept in cube for less than 2 sec = Failure
			if (exited_list_l[i] - entered_list_l[i]) < 1.5:
				l_result_info = " : Left Hand Failure"
				r_result_info = (r_result_info + l_result_info)
				info.setText(r_result_info)
				trial_result_l.append('failure')

			elif (exited_list_l[i] - entered_list_l[i]) >= 1.5:
				l_result_info = " : Left Hand Success"
				r_result_info = (r_result_info + l_result_info)
				info.setText(r_result_info)
				trial_result_l.append('success')


			# save events of trial
			row = (str(startTime) + ',' +
					str(size_id) + ',' +
					str(pos_id) + ',' +
					str(pos_r_box[0]) + ',' +
					str(pos_r_box[1]) + ',' +
					str(pos_r_box[2]) + ','+
					str(pos_id_r)+ ',' +
					trial_result_r[i] + "," +
					str(entered_list_r[i]) + "," +
					str(exited_list_r[i]) + "," +
					str(pos_l_box[0]) + ',' +
					str(pos_l_box[1]) + ',' +
					str(pos_l_box[2]) + ',' +
					str(pos_id_l)+ ',' +
					trial_result_l[i] + ","+
					str(entered_list_l[i]) + "," +
					str(exited_list_l[i]) +"\n")
			#print(row)
			yield csv.write(row)

			# counter + 2 so that we avoid calling left hand sensor from last trial
			# as right hand sensor for the next
			counter += 2


		# check which trial we are in
		print('Trial num: ', str(i))


	#save results
	info.setText('Thank You. You have completed this learning-phase')
	postimer.setEnabled(viz.OFF)
	print('right hand: ')
	print(entered_list_r)
	print(exited_list_r)
	print(trial_result_r)


	print('left hand: ')
	print(entered_list_l)
	print(exited_list_l)
	print(trial_result_l)

################################################################################################################
## TEST PHASE 2H
################################################################################################################

def testPhase_2H_position_difference(subject, height, dominant_hand, reaching_distance, head_height, shoulder_height, hip_height, right_pos, left_pos, middle):
	'''
	Two handed testphase. Presents participant with 2 boxes presented in one
	out of 9 possible positions each for every trial.
	Waits for participant to reach into a box to start trial, then displays box
	for 5 further seconds.
	Logs time for entering and exiting box.
	There is a 5 seconds waiting period after each trial, before new boxes are presented
	and a dedicated break after 2 Blocks, which can be skipped by pressing spacebar.

	input:
	(both result of the participantInfo function called at the beginnig of the exp)
	subject = subject ID
	height = subject height in meters
	dominant_hand = dominant hand of subject
	reaching_distance = approx. reaching distance of subject
	head_height = approx. head height of subject
	shoulder_height = approx. shoulder_height of subject
	hip_height = approx. hip height of subject
	right_pos = rightmost position for stimuli-box in z-dim
	left_pos = lefttmost position for stimuli-box in z-dim
	middle = 0 = middle position for stimuli-box in z-dim

	'''

	global info, entered_l, exited_l, entered_r, exited_r, entered_list_r, exited_list_r, trial_result_r, entered_list_l, exited_list_l, trial_result_l, debugging_mode


	entered_list_r = []
	exited_list_r = []
	trial_result_r = []

	entered_list_l = []
	exited_list_l = []
	trial_result_l = []

	now = datetime.datetime.now()  # get current time stamp to append to filename to avoid overwriting data on retries
	# open csv for to save movement data to
	csv_ = open('data/'+ 'sub-' + str(subject)+ '/' + 'sub-' + str(subject)+ '-2H-data-' + str(now.strftime("%Y_%m_%d_%H_%M")) + '.csv', 'w')
	# write column headers to csv
	columnTitleRow = "time,marker_0_x,marker_0_y,marker_0_z,marker_1_x,marker_1_y,marker_1_z,marker_2_x,marker_2_y,marker_2_z,marker_3_x,marker_3_y,marker_3_z,marker_4_x,marker_4_y,marker_4_z,marker_5_x,marker_5_y,marker_5_z,marker_6_x,marker_6_y,marker_6_z,marker_7_x,marker_7_y,marker_7_z,marker_8_x,marker_8_y,marker_8_z,marker_9_x,marker_9_y,marker_9_z,marker_10_x,marker_10_y,marker_10_z,marker_11_x,marker_11_y,marker_11_z,marker_12_x,marker_12_y,marker_12_z,marker_13_x,marker_13_y,marker_13_z,marker_14_x,marker_14_y,marker_14_z,marker_15_x,marker_15_y,marker_15_z,marker_16_x,marker_16_y,marker_16_z,marker_17_x,marker_17_y,marker_17_z,marker_18_x,marker_18_y,marker_18_z,marker_19_x,marker_19_y,marker_19_z,marker_20_x,marker_20_y,marker_20_z,marker_21_x,marker_21_y,marker_21_z,marker_22_x,marker_22_y,marker_22_z,marker_23_x,marker_23_y,marker_23_z,marker_24_x,marker_24_y,marker_24_z,marker_25_x,marker_25_y,marker_25_z,marker_26_x,marker_26_y,marker_26_z,marker_27_x,marker_27_y,marker_27_z,marker_28_x,marker_28_y,marker_28_z,marker_29_x,marker_29_y,marker_29_z,marker_30_x,marker_30_y,marker_30_z,marker_31_x,marker_31_y,marker_31_z,marker_32_x,marker_32_y,marker_32_z,marker_33_x,marker_33_y,marker_33_z,marker_34_x,marker_34_y,marker_34_z,marker_35_x,marker_35_y,marker_35_z,marker_36_x,marker_36_y,marker_36_z,marker_37_x,marker_37_y,marker_37_z\n"
	csv_.write(columnTitleRow)

	# open csv to save trial results and events for each hand
	csv = open('data/'+ 'sub-' + str(subject)+ '/' + 'sub-' + str(subject)+ '-2H-events-' + str(now.strftime("%Y_%m_%d_%H_%M")) + '.csv', 'w')
	# write column headers to csv
	columnTitleRow = "trial_start,box_size_id,box_pos_id,box_r_pos_x,box_r_pos_y,box_r_pos_z,box_pos_id_r,result_r,entered_r,exited_r,box_l_pos_x,box_l_pos_y,box_l_pos_z,box_pos_id_l,result_l,entered_l,exited_l\n"
	csv.write(columnTitleRow)


	# generate array of position identities, which will be called later on
	# might have to be changed to an explicit randomization procedure to balance trials
	arr_position = []
	arr = np.arange(13)
	arr = list(arr)
	# # range of trials
	trials = range(20)
	for j in trials:
		block = np.random.permutation(arr)
		for i in block:
			arr_position.append(block[i])

	# specify default pos  and size of target cube
	pos = [0,0,0]
	size_id = 's2'
	size = [0.20,0.20,0.20]
	size_offset = 0
	# call 'getpos' function every 0.1 sec to log movement data
	#vizact.ontimer(0.01666666666666666666666666666667, getpos, subject, csv_)
	postimer = vizact.ontimer(0.01666666666666666666666666666667, getpos, subject, csv_)

	# define counter to keep track of sensors later on
	counter = 0

	# iterate over range of trials
	for i in range(len(arr_position)):
		# set event flags to false
		entered_r = False
		exited_r = False

		entered_l = False
		exited_l = False

		if debugging_mode == 1:  # print a warning message when debugging mode is true
			print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DEBUGGING MODE ACTIVE : DATA WILL NOT BE SAVED  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

		# waiting period before next box is presented
		yield viztask.waitTime(1)
		# Update Instrcution
		info.setText('Testphase: Reach for the boxes')


		# boxes at approx. head height
		if arr_position[i] == 0:
			pos_r_box  = [reaching_distance + size_offset, head_height, right_pos]
			pos_l_box  = [reaching_distance + size_offset, head_height, left_pos]
			pos_id_r = 'r1'
			pos_id_l = 'l1'
			pos_id = 'r1-l1'
		elif arr_position[i] == 1:
			pos_r_box  = [reaching_distance + size_offset, head_height, middle]
			pos_l_box  = [reaching_distance + size_offset, head_height, left_pos]
			pos_id_r = 'm1'
			pos_id_l = 'l1'
			pos_id = 'm1-l1'
		elif arr_position[i] == 2:
			pos_r_box  = [reaching_distance + size_offset, head_height, right_pos]
			pos_l_box  = [reaching_distance + size_offset, head_height, middle]
			pos_id_r = 'r1'
			pos_id_l = 'm1'
			pos_id = 'r1-m1'

		# boxes at approx. chest height
		elif arr_position[i] == 3:
			pos_r_box  = [reaching_distance + size_offset,shoulder_height , right_pos]
			pos_l_box  = [reaching_distance + size_offset, shoulder_height, left_pos]
			pos_id_r = 'r2'
			pos_id_l = 'l2'
			pos_id = 'r2-l2'
		elif arr_position[i] == 4:
			pos_r_box  = [reaching_distance + size_offset, shoulder_height, middle]
			pos_l_box  = [reaching_distance + size_offset, shoulder_height, left_pos]
			pos_id_r = 'm2'
			pos_id_l = 'l2'
			pos_id = 'm2-l2'
		elif arr_position[i] == 5:
			pos_r_box  = [reaching_distance + size_offset, shoulder_height, right_pos]
			pos_l_box  = [reaching_distance + size_offset, shoulder_height, middle]
			pos_id_r = 'r2'
			pos_id_l = 'm2'
			pos_id = 'r2-m2'

		# boxes at approx. hip height
		elif arr_position[i] == 6:
			pos_r_box  = [reaching_distance + size_offset, hip_height, right_pos]
			pos_l_box  = [reaching_distance + size_offset, hip_height, left_pos]
			pos_id_r = 'r3'
			pos_id_l = 'l3'
			pos_id = 'r3-l3'
		elif arr_position[i] == 7:
			pos_r_box  = [reaching_distance + size_offset, hip_height, middle]
			pos_l_box  = [reaching_distance + size_offset, hip_height, left_pos]
			pos_id_r = 'm3'
			pos_id_l = 'l3'
			pos_id = 'm3-l3'
		elif arr_position[i] == 8:
			pos_r_box  = [reaching_distance + size_offset, hip_height, right_pos]
			pos_l_box  = [reaching_distance + size_offset, hip_height, middle]
			pos_id_r = 'r3'
			pos_id_l = 'm3'
			pos_id = 'r3-m3'

		# boxes at mixed heights
		elif arr_position[i] == 9:
			pos_r_box  = [reaching_distance + size_offset, head_height, right_pos]
			pos_l_box  = [reaching_distance + size_offset, hip_height, left_pos]
			pos_id_r = 'r1'
			pos_id_l = 'l3'
			pos_id = 'r1-l3'
		elif arr_position[i] == 10:
			pos_r_box  = [reaching_distance + size_offset, hip_height, right_pos]
			pos_l_box  = [reaching_distance + size_offset, head_height, left_pos]
			pos_id_r = 'r3'
			pos_id_l = 'l1'
			pos_id = 'r3-l1'
		elif arr_position[i] == 11:
			pos_r_box  = [reaching_distance + size_offset, head_height, middle]
			pos_l_box  = [reaching_distance + size_offset, hip_height, middle]
			pos_id_r = 'm1'
			pos_id_l = 'm3'
			pos_id = 'm1-m3'
		elif arr_position[i] == 12:
			pos_r_box  = [reaching_distance + size_offset, hip_height, middle]
			pos_l_box  = [reaching_distance + size_offset, head_height, middle]
			pos_id_r = 'm3'
			pos_id_l = 'm1'
			pos_id = 'm3-m1'

#		# setup start  box
#		while centerSensor not in manager_r.getActiveSensors():
#			yield vizproximity.waitEnter(centerSensor)
#		viz.playSound('beep.wav')
		if dominant_hand == 'l':
			while centerSensor not in manager_l.getActiveSensors():
				yield vizproximity.waitEnter(centerSensor)
		elif dominant_hand == 'r':
			while centerSensor not in manager_r.getActiveSensors():
				yield vizproximity.waitEnter(centerSensor)
		viz.playSound('beep.wav')

		#store the time at which this trial started
		startTime = time.time()
		print('started at: '+str(startTime))

		print(pos_id_r)
		print(pos_id_l)

		# setup r target box
		box_r = vizshape.addBox(size = size, alpha=0.5, color=[0.5,0.5,0])
		# set position of target
		box_r.setPosition(pos_r_box)

		# define a proximity sensor around target
		sensor_r = vizproximity.addBoundingBoxSensor(box_r,  scale=(1,1,1))
		#boxSensors.append(sensor_r)
		manager_r.addSensor(sensor_r)

		# setup l target box
		box_l = vizshape.addBox(size = size, alpha=0.5,color=[0,0,1])
		box_l.setPosition(pos_l_box)
		#print('pos_right' + str(pos_r_box))
		#print('pos_left' + str(pos_l_box))

		# define a proximity sensor around target
		sensor_l= vizproximity.addBoundingBoxSensor(box_l,  scale=(1,1,1))
		#boxSensors.append(sensor_l)
		manager_l.addSensor(sensor_l)

		# setup functions to log when participant entered and exited target boxes
		manager_r.onEnter(sensor_r, Enterbox_r, box_r, viz.RED)
		manager_r.onExit(sensor_r, Exitbox_r, box_r)

		manager_l.onEnter(sensor_l, Enterbox_l, box_l, viz.RED)
		manager_l.onExit(sensor_l, Exitbox_l, box_l)

		#Get sensors for this trial
		#sensor_r = boxSensors[counter]
		#sensor_l = boxSensors[counter+1]

		# Update Instrcution
		info.setText('Testphase: Reach for the box')

		if debugging_mode == 0:  # only applicable in VR-Lab
			# wait for participant to enter sensors
			con_r = viztask.waitTrue(getEnter_r)
			con_l = viztask.waitTrue(getEnter_l)
			d = yield viztask.waitAll([con_r, con_l])
			viz.playSound('beep.wav')

		# display target cube for 5 seconds after sensor has been entered
		yield viztask.waitTime(3)

		# remove right hand box
		box_r.remove()
		box_removed_r = time.time()
		# left hand
		box_l.remove()
		box_removed_l = time.time()

		if debugging_mode == 0:  # only applicable in VR-Lab
			try:
				# check if right hand box not exited
				print(exited_list_r[i])
			except IndexError:
				# append time that box was removed as endpoint if box not exited
				exited_list_r.append(box_removed_r)
				print('box_removed')
				
			try:
				# check if right hand box not exited
				print(exited_list_l[i])
			except IndexError:
				# append time that box was removed as endpoint if box not exited
				exited_list_l.append(box_removed_l)
				print('box_removed')

			print('entered: ', entered_list_r)
			print('exited: ', exited_list_r)

			# if hand was kept in cube for less than 2 sec = Failure
			if (exited_list_r[i] - entered_list_r[i]) < 1.5:
				r_result_info = "Right Hand Failure"
				info.setText(r_result_info)
				trial_result_r.append('failure')

			elif (exited_list_r[i] - entered_list_r[i]) >= 1.5:
				r_result_info = "Right Hand Success"
				info.setText(r_result_info)
				trial_result_r.append('success')

			# if hand was kept in cube for less than 2 sec = Failure
			if (exited_list_l[i] - entered_list_l[i]) < 1.5:
				l_result_info = " : Left Hand Failure"
				r_result_info = (r_result_info + l_result_info)
				info.setText(r_result_info)
				trial_result_l.append('failure')

			elif (exited_list_l[i] - entered_list_l[i]) >= 1.5:
				l_result_info = " : Left Hand Success"
				r_result_info = (r_result_info + l_result_info)
				info.setText(r_result_info)
				trial_result_l.append('success')

			# save events of trial
			row = (str(startTime) + ',' +
					str(size_id) + ',' +
					str(pos_id) + ',' +
					str(pos_r_box[0]) + ',' +
					str(pos_r_box[1]) + ',' +
					str(pos_r_box[2]) + ','+
					str(pos_id_r)+ ',' +
					trial_result_r[i] + "," +
					str(entered_list_r[i]) + "," +
					str(exited_list_r[i]) + "," +
					str(pos_l_box[0]) + ',' +
					str(pos_l_box[1]) + ',' +
					str(pos_l_box[2]) + ',' +
					str(pos_id_l)+ ',' +
					trial_result_l[i] + ","+
					str(entered_list_l[i]) + "," +
					str(exited_list_l[i]) +"\n")
			csv.write(row)

			# counter + 2 so that we avoid calling left hand sensor from last trial
			# as right hand sensor for the next
			counter += 2


		# check which trial we are in
		print('Trial num: ', str(i))
		# break after 26 trials
		if ((i-1) % 26) == 0 and i > 1:
			info.setText('Break')
			# wait for button press to continue experiment
			yield viztask.waitKeyDown(' ')

	#save results
	info.setText('Thank You. You have completed the second Testphase')
	postimer.setEnabled(viz.OFF)
	print('right hand: ')
	print(entered_list_r)
	print(exited_list_r)
	print(trial_result_r)

	print('left hand: ')
	print(entered_list_l)
	print(exited_list_l)
	print(trial_result_l)

################################################################################################################
## LEARNING PHASE 2H SIZE DIFFERENCE
################################################################################################################

def learningPhase_2H_size_difference(subject, height, dominant_hand, reaching_distance, head_height, shoulder_height, hip_height, right_pos, left_pos, middle):
	'''
	Two handed learningphase. Presents participant with 2 boxes presented in one
	out of 3 different sizes every trial.
	Waits for participant to reach into a box to start trial, then displays box
	for 5 further seconds.
	Logs time for entering and exiting box.
	There is a 5 seconds waiting period after each trial, before new boxes are presented
	and a dedicated break after 2 Blocks, which can be skipped by pressing spacebar.

	input:
	(both result of the participantInfo function called at the beginnig of the exp)
	subject = subject ID
	height = subject height in meters
	dominant_hand = dominant hand of subject
	reaching_distance = approx. reaching distance of subject
	head_height = approx. head height of subject
	shoulder_height = approx. shoulder_height of subject
	hip_height = approx. hip height of subject
	right_pos = rightmost position for stimuli-box in z-dim
	left_pos = lefttmost position for stimuli-box in z-dim
	middle = 0 = middle position for stimuli-box in z-dim

	'''

	global info, entered_l, exited_l, entered_r, exited_r, entered_list_r, exited_list_r, trial_result_r, entered_list_l, exited_list_l, trial_result_l, debugging_mode

	now = datetime.datetime.now()  # get current time stamp to append to filename to avoid overwriting data on retries
	# open csv for to save movement data to
	csv_ = open('data/'+ 'sub-' + str(subject)+ '/' + 'sub-' + str(subject)+ '-2H-size_diff_learning_data_' + str(now.strftime("%Y_%m_%d_%H_%M")) + '.csv', 'w')
	# write column headers to csv
	columnTitleRow = "time,marker_0_x,marker_0_y,marker_0_z,marker_1_x,marker_1_y,marker_1_z,marker_2_x,marker_2_y,marker_2_z,marker_3_x,marker_3_y,marker_3_z,marker_4_x,marker_4_y,marker_4_z,marker_5_x,marker_5_y,marker_5_z,marker_6_x,marker_6_y,marker_6_z,marker_7_x,marker_7_y,marker_7_z,marker_8_x,marker_8_y,marker_8_z,marker_9_x,marker_9_y,marker_9_z,marker_10_x,marker_10_y,marker_10_z,marker_11_x,marker_11_y,marker_11_z,marker_12_x,marker_12_y,marker_12_z,marker_13_x,marker_13_y,marker_13_z,marker_14_x,marker_14_y,marker_14_z,marker_15_x,marker_15_y,marker_15_z,marker_16_x,marker_16_y,marker_16_z,marker_17_x,marker_17_y,marker_17_z,marker_18_x,marker_18_y,marker_18_z,marker_19_x,marker_19_y,marker_19_z,marker_20_x,marker_20_y,marker_20_z,marker_21_x,marker_21_y,marker_21_z,marker_22_x,marker_22_y,marker_22_z,marker_23_x,marker_23_y,marker_23_z,marker_24_x,marker_24_y,marker_24_z,marker_25_x,marker_25_y,marker_25_z,marker_26_x,marker_26_y,marker_26_z,marker_27_x,marker_27_y,marker_27_z,marker_28_x,marker_28_y,marker_28_z,marker_29_x,marker_29_y,marker_29_z,marker_30_x,marker_30_y,marker_30_z,marker_31_x,marker_31_y,marker_31_z,marker_32_x,marker_32_y,marker_32_z,marker_33_x,marker_33_y,marker_33_z,marker_34_x,marker_34_y,marker_34_z,marker_35_x,marker_35_y,marker_35_z,marker_36_x,marker_36_y,marker_36_z,marker_37_x,marker_37_y,marker_37_z\n"
	csv_.write(columnTitleRow)

	csv = open('data/'+ 'sub-' + str(subject)+ '/' + 'sub-' + str(subject)+ '-2H-size_diff_learning_events_' + str(now.strftime("%Y_%m_%d_%H_%M")) + '.csv', 'w')
	# write column headers to csv
	columnTitleRow = "trial_start,box_size_id,box_r_pos_x,box_r_pos_y,box_r_pos_z,box_pos_id_r,box_size_r,result_r,entered_r,exited_r,box_l_pos_x,box_l_pos_y,box_l_pos_z,box_pos_id_l,box_size_l,result_l,entered_l,exited_l\n"
	csv.write(columnTitleRow)

	# generate array of size identities, which will be called later on
	arr_size = []
	arr = np.arange(6)
	arr = list(arr)
	# # range of trials
	trials = range(2)
	for j in trials:
		block = np.random.permutation(arr)
		for i in block:
			arr_size.append(block[i])

	# call 'getpos' function every 0.1 sec to log movement data
	vizact.ontimer(0.01666666666666666666666666666667, getpos, subject, csv_)

	# define counter to keep track of sensors later on
	counter = 0

	# iterate over range of trials
	for i in range(len(arr_size)):
		# set event flags to false
		entered_r = False
		exited_r = False

		entered_l = False
		exited_l = False

		if debugging_mode == 1:  # print a warning message when debugging mode is true
			print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DEBUGGING MODE ACTIVE : DATA WILL NOT BE SAVED  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

		# waiting period before next box is presented
		yield viztask.waitTime(1)
		# Update Instrcution
		info.setText('Testphase: Reach for the boxes')


		# define box sizes
		small = [0.15,0.15,0.15]
		medium = [0.20,0.20,0.20]
		large = [0.25,0.25,0.25]
		# display boxes in differnt size configurations
		if arr_size[i] == 0:
			size_r = small
			size_l = medium
			size_id = 'r_s1-l_s2'
		elif arr_size[i] == 1:
			size_r = small
			size_l = large
			size_id = 'r_s1-l_s3'
		elif arr_size[i] == 2:
			size_r = medium
			size_l = small
			size_id = 'r_s2-l_s1'
		elif arr_size[i] == 3:
			size_r = large
			size_l = small
			size_id = 'r_s3-l_s1'
		elif arr_size[i] == 4:
			size_r = medium
			size_l = large
			size_id = 'r_s2-l_s3'
		elif arr_size[i] == 5:
			size_r = large
			size_l = medium
			size_id = 'r_s3-l_s2'

		print(size_id)

		# specify pos of target cube; compensate for size difference
		size_offset_small_box = .025
		size_offset_large_box = -.025
		if size_id == 'r_s1-l_s2':
			pos_r_box  = [reaching_distance + size_offset_small_box , shoulder_height, right_pos]
			pos_l_box  = [reaching_distance, shoulder_height, left_pos]
		elif size_id == 'r_s1-l_s3':
			pos_r_box  = [reaching_distance + size_offset_small_box, shoulder_height, right_pos]
			pos_l_box  = [reaching_distance + size_offset_large_box, shoulder_height, left_pos]
		elif size_id == 'r_s2-l_s1':
			pos_r_box  = [reaching_distance, shoulder_height, right_pos]
			pos_l_box  = [reaching_distance + size_offset_small_box, shoulder_height, left_pos]
		elif size_id == 'r_s3-l_s1':
			pos_r_box  = [reaching_distance + size_offset_large_box, shoulder_height, right_pos]
			pos_l_box  = [reaching_distance + size_offset_small_box, shoulder_height, left_pos]
		elif size_id == 'r_s2-l_s3':
			pos_r_box  = [reaching_distance, shoulder_height, right_pos]
			pos_l_box  = [reaching_distance + size_offset_large_box, shoulder_height, left_pos]
		elif size_id == 'r_s3-l_s2':
			pos_r_box  = [reaching_distance + size_offset_large_box, shoulder_height, right_pos]
			pos_l_box  = [reaching_distance, shoulder_height, left_pos]

		# setup start  box
		while centerSensor not in manager_r.getActiveSensors():
			yield vizproximity.waitEnter(centerSensor)
		viz.playSound('beep.wav')
		#store the time at which this movement started
		startTime = time.time()
		print('started at: '+str(startTime))

		pos_id_r = 'r2'
		pos_id_l = 'l2'
		# setup target box
		box_r = vizshape.addBox(size = size_r, alpha=0.5, color=[0.5,0.5,0])
		# set position of target
		box_r.setPosition(pos_r_box)

		# define a proximity sensor around target
		sensor_r = vizproximity.addBoundingBoxSensor(box_r,  scale=(1,1,1))
		#boxSensors.append(sensor_r)
		manager_r.addSensor(sensor_r)

		# setup target box
		box_l = vizshape.addBox(size = size_l, alpha=0.5, color=[0,0,1])
		box_l.setPosition(pos_l_box)
		print('pos_right' + str(pos_r_box))
		print('pos_left' + str(pos_l_box))

		# define a proximity sensor around target
		sensor_l= vizproximity.addBoundingBoxSensor(box_l,  scale=(1,1,1))
		#boxSensors.append(sensor_l)
		manager_l.addSensor(sensor_l)

		# setup functions to log when participant entered and exited target boxes
		manager_r.onEnter(sensor_r, Enterbox_r, box_r, viz.RED)
		manager_r.onExit(sensor_r, Exitbox_r, box_r)

		manager_l.onEnter(sensor_l, Enterbox_l, box_l, viz.RED)
		manager_l.onExit(sensor_l, Exitbox_l, box_l)

		#Get sensors for this trial
		#sensor_r = boxSensors[counter]
		#sensor_l = boxSensors[counter+1]


		# Update Instrcution
		info.setText('Learningphase: Reach for the box')

		if debugging_mode == 0:  # only applicable in VR-Lab
			# wait for participant to enter sensors
			con_r = viztask.waitTrue(getEnter_r)
			con_l = viztask.waitTrue(getEnter_l)
			d = yield viztask.waitAll([con_r, con_l])
			viz.playSound('beep.wav')

			#print "Hi"
		# display target cube for 3 seconds after sensor has been entered
		yield viztask.waitTime(3)

		# remove right hand box
		box_r.remove()
		box_removed_r = time.time()
		# left hand
		box_l.remove()
		box_removed_l = time.time()

		if debugging_mode == 0:  # only applicable in VR-Lab
			try:
				# check if right hand box not exited
				print(exited_list_r[i])
			except IndexError:
				# append time that box was removed as endpoint if box not exited
				exited_list_r.append(box_removed_r)
				print('box_removed')

			print('entered: ', entered_list_r)
			print('exited: ', exited_list_r)

			# if hand was kept in cube for less than 2 sec = Failure
			if (exited_list_r[i] - entered_list_r[i]) < 1.5:
				r_result_info = "Right Hand Failure"
				info.setText(r_result_info)
				trial_result_r.append('failure')

			elif (exited_list_r[i] - entered_list_r[i]) >= 1.5:
				r_result_info = "Right Hand Success"
				info.setText(r_result_info)
				trial_result_r.append('success')

			# same for left hand box
			try:
				# check if right hand box not exited
				print(exited_list_l[i])
			except IndexError:
				# append time that box was removed as endpoint if box not exited
				exited_list_l.append(box_removed_l)
				print('box_removed')

			#print('entered_l: ', entered_list_l)
			#print('exited_l: ', exited_list_l)

			# if hand was kept in cube for less than 2 sec = Failure
			if (exited_list_l[i] - entered_list_l[i]) < 1.5:
				l_result_info = " : Left Hand Failure"
				r_result_info = (r_result_info + l_result_info)
				info.setText(r_result_info)
				trial_result_l.append('failure')

			elif (exited_list_l[i] - entered_list_l[i]) >= 1.5:
				l_result_info = " : Left Hand Success"
				r_result_info = (r_result_info + l_result_info)
				info.setText(r_result_info)
				trial_result_l.append('success')

			# save right hand results of trial
			row = (str(startTime) + ',' +
					str(size_id) + ',' +
					str(pos_r_box[0]) + ',' +
					str(pos_r_box[1]) + ',' +
					str(pos_r_box[2]) + ',' +
					str(pos_id_r)+ ',' +
					str(size_r[0]) + ',' +
					trial_result_r[i] + ',' +
					str(entered_list_r[i]) + ',' +
					str(exited_list_r[i]) + ',' +
					str(pos_l_box[0]) + ',' +
					str(pos_l_box[1]) + ',' +
					str(pos_l_box[2]) + ',' +
					str(pos_id_l)+ ',' +
					str(size_l[0]) + ',' +
					trial_result_l[i] + ',' +
					str(entered_list_l[i]) + ',' +
					str(exited_list_l[i]) +"\n")
			csv.write(row)

			# counter + 2 so that we avoid calling left hand sensor from last trial
			# as right hand sensor for the next
			counter += 2


		# check which trial we are in
		print('Trial num: ', str(i))
#		# break after 8 trials
#		if ((i-1) % 12) == 0 and i > 1:
#			info.setText('Break')
#			# wait for button press to continue experiment
#			yield viztask.waitKeyDown(' ')


	#save results
	info.setText('Thank You. You have completed this learning-phase')
	print('right hand: ')
	print(entered_list_r)
	print(exited_list_r)
	print(trial_result_r)


	print('left hand: ')
	print(entered_list_l)
	print(exited_list_l)
	print(trial_result_l)

################################################################################################################
## TEST PHASE 2H SIZE DIFFERENCE
################################################################################################################

def testPhase_2H_size_difference(subject, height, dominant_hand, reaching_distance, head_height, shoulder_height, hip_height, right_pos, left_pos, middle):
	'''
	Two handed testphase. Presents participant with 2 boxes presented in one
	out of 3 different sizes every trial.
	Waits for participant to reach into a box to start trial, then displays box
	for 5 further seconds.
	Logs time for entering and exiting box.
	There is a 5 seconds waiting period after each trial, before new boxes are presented
	and a dedicated break after 2 Blocks, which can be skipped by pressing spacebar.

	input:
	(both result of the participantInfo function called at the beginnig of the exp)
	subject = subject ID
	height = subject height in meters
	dominant_hand = dominant hand of subject
	reaching_distance = approx. reaching distance of subject
	head_height = approx. head height of subject
	shoulder_height = approx. shoulder_height of subject
	hip_height = approx. hip height of subject
	right_pos = rightmost position for stimuli-box in z-dim
	left_pos = lefttmost position for stimuli-box in z-dim
	middle = 0 = middle position for stimuli-box in z-dim

	'''

	global info, entered_l, exited_l, entered_r, exited_r, entered_list_r, exited_list_r, trial_result_r, entered_list_l, exited_list_l, trial_result_l, debugging_mode

	now = datetime.datetime.now()  # get current time stamp to append to filename to avoid overwriting data on retries
	# open csv for to save movement data to
	csv_ = open('data/'+ 'sub-' + str(subject)+ '/' + 'sub-' + str(subject)+ '-2H-size_diff_data_' + str(now.strftime("%Y_%m_%d_%H_%M")) + '.csv', 'w')
	# write column headers to csv
	columnTitleRow = "time,marker_0_x,marker_0_y,marker_0_z,marker_1_x,marker_1_y,marker_1_z,marker_2_x,marker_2_y,marker_2_z,marker_3_x,marker_3_y,marker_3_z,marker_4_x,marker_4_y,marker_4_z,marker_5_x,marker_5_y,marker_5_z,marker_6_x,marker_6_y,marker_6_z,marker_7_x,marker_7_y,marker_7_z,marker_8_x,marker_8_y,marker_8_z,marker_9_x,marker_9_y,marker_9_z,marker_10_x,marker_10_y,marker_10_z,marker_11_x,marker_11_y,marker_11_z,marker_12_x,marker_12_y,marker_12_z,marker_13_x,marker_13_y,marker_13_z,marker_14_x,marker_14_y,marker_14_z,marker_15_x,marker_15_y,marker_15_z,marker_16_x,marker_16_y,marker_16_z,marker_17_x,marker_17_y,marker_17_z,marker_18_x,marker_18_y,marker_18_z,marker_19_x,marker_19_y,marker_19_z,marker_20_x,marker_20_y,marker_20_z,marker_21_x,marker_21_y,marker_21_z,marker_22_x,marker_22_y,marker_22_z,marker_23_x,marker_23_y,marker_23_z,marker_24_x,marker_24_y,marker_24_z,marker_25_x,marker_25_y,marker_25_z,marker_26_x,marker_26_y,marker_26_z,marker_27_x,marker_27_y,marker_27_z,marker_28_x,marker_28_y,marker_28_z,marker_29_x,marker_29_y,marker_29_z,marker_30_x,marker_30_y,marker_30_z,marker_31_x,marker_31_y,marker_31_z,marker_32_x,marker_32_y,marker_32_z,marker_33_x,marker_33_y,marker_33_z,marker_34_x,marker_34_y,marker_34_z,marker_35_x,marker_35_y,marker_35_z,marker_36_x,marker_36_y,marker_36_z,marker_37_x,marker_37_y,marker_37_z\n"
	csv_.write(columnTitleRow)

	csv = open('data/'+ 'sub-' + str(subject)+ '/' + 'sub-' + str(subject)+ '-2H-size_diff_events_' + str(now.strftime("%Y_%m_%d_%H_%M")) + '.csv', 'w')
	# write column headers to csv
	columnTitleRow = "trial_start,box_size_id,box_r_pos_x,box_r_pos_y,box_r_pos_z,box_pos_id_r,box_size_r,result_r,entered_r,exited_r,box_l_pos_x,box_l_pos_y,box_l_pos_z,box_pos_id_l,box_size_l,result_l,entered_l,exited_l\n"
	csv.write(columnTitleRow)

	# generate array of size identities, which will be called later on
	arr_size = []
	arr = np.arange(6)
	arr = list(arr)
	# # range of trials
	trials = range(20)
	for j in trials:
		block = np.random.permutation(arr)
		for i in block:
			arr_size.append(block[i])

	# call 'getpos' function every 0.1 sec to log movement data
	vizact.ontimer(0.01666666666666666666666666666667, getpos, subject, csv_)

	# define counter to keep track of sensors later on
	counter = 0

	# iterate over range of trials
	for i in range(len(arr_size)):
		# set event flags to false
		entered_r = False
		exited_r = False

		entered_l = False
		exited_l = False

		if debugging_mode == 1:  # print a warning message when debugging mode is true
			print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DEBUGGING MODE ACTIVE : DATA WILL NOT BE SAVED  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

		# waiting period before next box is presented
		yield viztask.waitTime(1)
		# Update Instrcution
		info.setText('Testphase: Reach for the boxes')

		# define box sizes
		small = [0.15,0.15,0.15]
		medium = [0.20,0.20,0.20]
		large = [0.25,0.25,0.25]
		# display boxes in differnt size configurations
		if arr_size[i] == 0:
			size_r = small
			size_l = medium
			size_id = 'r_s1-l_s2'
		elif arr_size[i] == 1:
			size_r = small
			size_l = large
			size_id = 'r_s1-l_s3'
		elif arr_size[i] == 2:
			size_r = medium
			size_l = small
			size_id = 'r_s2-l_s1'
		elif arr_size[i] == 3:
			size_r = large
			size_l = small
			size_id = 'r_s3-l_s1'
		elif arr_size[i] == 4:
			size_r = medium
			size_l = large
			size_id = 'r_s2-l_s3'
		elif arr_size[i] == 5:
			size_r = large
			size_l = medium
			size_id = 'r_s3-l_s2'

		print(size_id)

		# specify pos of target cube; compensate for size difference
		size_offset_small_box = .025
		size_offset_large_box = -.025
		if size_id == 'r_s1-l_s2':
			pos_r_box  = [reaching_distance + size_offset_small_box , shoulder_height, right_pos]
			pos_l_box  = [reaching_distance, shoulder_height, left_pos]
		elif size_id == 'r_s1-l_s3':
			pos_r_box  = [reaching_distance + size_offset_small_box, shoulder_height, right_pos]
			pos_l_box  = [reaching_distance + size_offset_large_box, shoulder_height, left_pos]
		elif size_id == 'r_s2-l_s1':
			pos_r_box  = [reaching_distance, shoulder_height, right_pos]
			pos_l_box  = [reaching_distance + size_offset_small_box, shoulder_height, left_pos]
		elif size_id == 'r_s3-l_s1':
			pos_r_box  = [reaching_distance + size_offset_large_box, shoulder_height, right_pos]
			pos_l_box  = [reaching_distance + size_offset_small_box, shoulder_height, left_pos]
		elif size_id == 'r_s2-l_s3':
			pos_r_box  = [reaching_distance, shoulder_height, right_pos]
			pos_l_box  = [reaching_distance + size_offset_large_box, shoulder_height, left_pos]
		elif size_id == 'r_s3-l_s2':
			pos_r_box  = [reaching_distance + size_offset_large_box, shoulder_height, right_pos]
			pos_l_box  = [reaching_distance, shoulder_height, left_pos]

		# setup start box
		while centerSensor not in manager_r.getActiveSensors():
			yield vizproximity.waitEnter(centerSensor)
		viz.playSound('beep.wav')
		#store the time at which this move started
		startTime = time.time()
		print('started at: '+str(startTime))


		pos_id_r = 'r2'
		pos_id_l = 'l2'
		# setup target box
		box_r = vizshape.addBox(size = size_r, alpha=0.5,  color=[0.5,0.5,0])
		# set position of target
		box_r.setPosition(pos_r_box)

		# define a proximity sensor around target
		sensor_r = vizproximity.addBoundingBoxSensor(box_r,  scale=(1,1,1))
		#boxSensors.append(sensor_r)
		manager_r.addSensor(sensor_r)

		# setup target box
		box_l = vizshape.addBox(size = size_l, alpha=0.5,  color=[0,0,1])
		box_l.setPosition(pos_l_box)
		print('pos_right' + str(pos_r_box))
		print('pos_left' + str(pos_l_box))

		# define a proximity sensor around target
		sensor_l= vizproximity.addBoundingBoxSensor(box_l,  scale=(1,1,1))
		#boxSensors.append(sensor_l)
		#print(boxSensors)
		manager_l.addSensor(sensor_l)

		# setup functions to log when participant entered and exited target boxes
		manager_r.onEnter(sensor_r, Enterbox_r, box_r, viz.RED)
		manager_r.onExit(sensor_r, Exitbox_r, box_r)

		manager_l.onEnter(sensor_l, Enterbox_l, box_l, viz.RED)
		manager_l.onExit(sensor_l, Exitbox_l, box_l)

		#Get sensors for this trial
		#sensor_r = boxSensors[counter]
		#sensor_l = boxSensors[counter+1]


		# Update Instrcution
		info.setText('Testphase: Reach for the box')

		if debugging_mode == 0:  # only applicable in VR-Lab
			# wait for participant to enter sensors
			con_r = viztask.waitTrue(getEnter_r)
			con_l = viztask.waitTrue(getEnter_l)
			d = yield viztask.waitAll([con_r, con_l])
			viz.playSound('beep.wav')

		# display target cube for 5 seconds after sensor has been entered
		yield viztask.waitTime(3)

		# remove right hand box
		box_r.remove()
		box_removed_r = time.time()
		# left hand
		box_l.remove()
		box_removed_l = time.time()

		if debugging_mode == 0:  # only applicable in VR-Lab
			try:
				# check if right hand box not exited
				print(exited_list_r[i])
			except IndexError:
				# append time that box was removed as endpoint if box not exited
				exited_list_r.append(box_removed_r)
				print('box_removed')

			#print('entered: ', entered_list_r)
			#print('exited: ', exited_list_r)

			# if hand was kept in cube for less than 2 sec = Failure
			if (exited_list_r[i] - entered_list_r[i]) < 1.5:
				r_result_info = "Right Hand Failure"
				info.setText(r_result_info)
				trial_result_r.append('failure')

			elif (exited_list_r[i] - entered_list_r[i]) >= 1.5:
				r_result_info = "Right Hand Success"
				info.setText(r_result_info)
				trial_result_r.append('success')

			# same for left hand box
			try:
				# check if right hand box not exited
				print(exited_list_l[i])
			except IndexError:
				# append time that box was removed as endpoint if box not exited
				exited_list_l.append(box_removed_l)
				print('box_removed')

			#print('entered_l: ', entered_list_l)
			#print('exited_l: ', exited_list_l)

			# if hand was kept in cube for less than 2 sec = Failure
			if (exited_list_l[i] - entered_list_l[i]) < 1.5:
				l_result_info = " : Left Hand Failure"
				r_result_info = (r_result_info + l_result_info)
				info.setText(r_result_info)
				trial_result_l.append('failure')

			elif (exited_list_l[i] - entered_list_l[i]) >= 1.5:
				l_result_info = " : Left Hand Success"
				r_result_info = (r_result_info + l_result_info)
				info.setText(r_result_info)
				trial_result_l.append('success')


			# save right hand results of trial
			row = (str(startTime) + ',' +
					str(size_id) + ',' +
					str(pos_r_box[0]) + ',' +
					str(pos_r_box[1]) + ',' +
					str(pos_r_box[2]) + ','+
					str(pos_id_r)+ ',' +
					str(size_r[0]) + ',' +
					trial_result_r[i] + "," +
					str(entered_list_r[i]) + "," +
					str(exited_list_r[i]) + "," +
					str(pos_l_box[0]) + ',' +
					str(pos_l_box[1]) + ',' +
					str(pos_l_box[2]) + ',' +
					str(pos_id_l)+ ',' +
					str(size_l[0]) + ',' +
					trial_result_l[i] + ","+
					str(entered_list_l[i]) + "," +
					str(exited_list_l[i]) +"\n")
			csv.write(row)

			# counter + 2 so that we avoid calling left hand sensor from last trial
			# as right hand sensor for the next
			counter += 2


		# check which trial we are in
		print('Trial num: ', str(i))
		# break after 8 trials (2Blocks)
		if ((i-1) % 24) == 0 and i > 1:
			info.setText('Break')
			# wait for button press to continue experiment
			yield viztask.waitKeyDown(' ')
		r_result_info = "Right Hand Success"
		info.setText(r_result_info)

	#save results
	info.setText('Thank You. You have completed the experiment')
	print('right hand: ')
	print(entered_list_r)
	print(exited_list_r)
	print(trial_result_r)

	print('left hand: ')
	print(entered_list_l)
	print(exited_list_l)
	print(trial_result_l)


def participantInfo():
	''' get and return particpant ID, height, handedness
	'''
	# get ID
	ID = vizinput.input('Subject ID:', parent=0)
	# get Height
	height = vizinput.input('Height in meteres (divided by "."):', parent=0)
	# get dominant Hand
	dominant_hand = vizinput.input('Dominant Hand (type "r" or "l"):', parent=0)
	# create subject directory
	try:
		os.makedirs('data/'+ 'sub-' + str(ID))
	except OSError as e:
		if e.errno != errno.EEXIST:
			raise
	return ID, height, dominant_hand  #return ID etc.



def experiment():
	''' function to schedule experiment:

		1. participantInfo()
			Ask for participant ID & Height
		2. scale Avatar to participants height
		3. d = yield viztask.waitKeyDown('s')
			wait for button press to start experiment and recording
		4. yield learning_Phase_1H
			start one handed task
		5. yield viztask.waitKeyDown(' ')
			wait for experimenter to press spacebar to continue exp
		6. yield test_Phase_1H
			start one handed task
		7. yield viztask.waitKeyDown(' ')
			wait for experimenter to press spacebar to continue exp
		8. yield learning_Phase_2H_position_diff
			start two handed task
		9. yield viztask.waitKeyDown(' ')
			wait for experimenter to press spacebar to continue exp
		10. yield tesPhase_2H_position_diff
			start two handed task
		11. yield learning_Phase_2H_size_diff
			start two handed task
		12. yield viztask.waitKeyDown(' ')
			wait for experimenter to press spacebar to continue exp
		13. yield tesPhase_2H_size_diff
			start two handed task
	'''

	global avatar
	subject, height, dominant_hand = participantInfo()
	height = float(height)


	# viz "Documentation" recommends calibrating avatar in t-pose
	# Press "C" to calibrate

	# configurations of a stimuli positions
	reaching_distance = -((height/2) -.30)  # half of armspan - 20cm to comfortably reach every box (+1 for origing point in lab)
	head_height = (height - (height/7)) + .2
	shoulder_height = (height - (height/7))
	hip_height = (height - (height/7)) - .2
	right_pos = .26
	middle = 0
	left_pos = -.26
	if dominant_hand== 'r':
			# sensor for starting trials
		manager_r.addSensor(centerSensor)
	elif dominant_hand == 'l':
		manager_l.addSensor(centerSensor)


	# press "s" button to start experiment and recording
	d = yield viztask.waitKeyDown('s')
	print(d)
	if d.key == 's':
		# save time at which exp was started and write to file
		now = datetime.datetime.now()  # get current time stamp to append to filename to avoid overwriting data on retries
		csv_parameters = open('data/'+ 'sub-' + str(subject)+ '/' + 'sub-' + str(subject)+ '_subject_parameters_' + str(now.strftime("%Y_%m_%d_%H_%M")) + '.csv', 'w')
		columnTitleRow = "subject,height,handedness,epoch_started\n"
		csv_parameters.write(columnTitleRow)
		row = str(subject) +  "," +  str(height)+  "," +  str(dominant_hand)+  "," + str(time.time())
		csv_parameters.write(row)
		print('better have started your recap2 recording')

	info.setText('Wait for box to appear')
	# start first learning phase
	yield learningPhase_1H(subject, height, dominant_hand, reaching_distance, head_height, shoulder_height, hip_height, right_pos, left_pos, middle)
	yield viztask.waitKeyDown(' ')  # wait for experimenter to press spacebar
#  start one-handed task
	yield testPhase_1H(subject, height, dominant_hand, reaching_distance, head_height, shoulder_height, hip_height, right_pos, left_pos, middle)
	yield viztask.waitKeyDown(' ')  # wait for experimenter to press spacebar
	# start two-handed_pos learning phase
	yield learningPhase_2H_position_difference(subject, height, dominant_hand, reaching_distance, head_height, shoulder_height, hip_height, right_pos, left_pos, middle)
	yield viztask.waitKeyDown(' ')  # wait for experimenter to press spacebar
	# start two-handed_pos_diff_task
	yield testPhase_2H_position_difference(subject, height, dominant_hand, reaching_distance, head_height, shoulder_height, hip_height, right_pos, left_pos, middle)
	yield viztask.waitKeyDown(' ')  # wait for experimenter to press spacebar
	# start two-handed learning phase
#	yield learningPhase_2H_size_difference(subject, height, dominant_hand, reaching_distance, head_height, shoulder_height, hip_height, right_pos, left_pos, middle)
#	yield viztask.waitKeyDown(' ')  # wait for experimenter to press spacebar
	# start two-handed_size_diff_task
#	yield testPhase_2H_size_difference(subject, height, dominant_hand, reaching_distance, head_height, shoulder_height, hip_height, right_pos, left_pos, middle)

################################################################################################################
## schedule experiment
################################################################################################################
viztask.schedule(experiment)
# experiment scheduler
info = vizinfo.InfoPanel("wait for experiment to start")
