#!/usr/bin/env python
# coding:utf-8
 
#from xml.etree.ElementTree import Element, SubElement, tostring
from lxml.etree import Element, SubElement, tostring
import pprint
from xml.dom.minidom import parseString
import numpy as np
CLASSES = ( 'speed limit 20', 'speed limit 30', 'speed limit 50', 'speed limit 60',
	'speed limit 70', 'speed limit 80', 'restriction ends 80', 'speed limit 100', 'speed limit 120',
	'no overtaking', 'no overtaking (trucks)', 'priority at next intersection', 'priority road',
	'give way', 'stop', 'no traffic both ways',
	'no trucks', 'no entry', 'danger', 'bend left','bend right', 'bend', 'uneven road',
	'slippery road ', 'slippery road', 'road narrows', 'construction','traffic signal', 'pedestrian crossing', 'school crossing',
	'cycles crossing', 'snow', 'animals', 'restriction ends',
	'go right', 'go left', 'go straight', 'go right or straight','keep right',
	'keep left ', 'roundabout', 'restriction ends', 'restriction ends')





with open("gt_train.txt","r") as f:
	lines = f.readlines()
	for i in range(len(lines)):
		node_root = Element('annotation')
 
		node_folder = SubElement(node_root, 'folder')
		node_folder.text = 'TrainIJCNN2013'
		line=lines[i].split(';')
		line_shape = np.reshape(line[1:],(-1,5))

		node_filename = SubElement(node_root, 'filename')
		img_name = line[0].split('.')[0]
		node_filename.text = line[0]

		node_size = SubElement(node_root, 'size')
		node_width = SubElement(node_size, 'width')
		node_width.text = '1360'
		 
		node_height = SubElement(node_size, 'height')
		node_height.text = '800'

		node_depth = SubElement(node_size, 'depth')
		node_depth.text = '3'

		for j in range(len(line_shape[:,4])):
			node_object = SubElement(node_root, 'object')

			node_name = SubElement(node_object, 'name')
			class_n=int(line_shape[:,4][j])
			node_name.text = CLASSES[class_n]

			#node_difficult = SubElement(node_object, 'difficult')
			#node_difficult.text = '0'

			node_bndbox = SubElement(node_object, 'bndbox')
			node_xmin = SubElement(node_bndbox, 'xmin')
			node_xmin.text = line_shape[:,0][j]
			node_ymin = SubElement(node_bndbox, 'ymin')
			node_ymin.text = line_shape[:,1][j]
			node_xmax = SubElement(node_bndbox, 'xmax')
			node_xmax.text = line_shape[:,2][j]
			node_ymax = SubElement(node_bndbox, 'ymax')
			node_ymax.text = line_shape[:,3][j]
		Xml = tostring(node_root, pretty_print=True)  #Formatted display, the newline of the newline
		#dom = parseString(Xml)

		with open("train_anno_xml/"+img_name+".xml","wb") as f:
			f.write(Xml)


