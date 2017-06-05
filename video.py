"""
Run the online classification system.
Capture an image, classify, do it again.
"""
import numpy as np
import tensorflow as tf
import time
from SimpleCV import *
import sys
import glob
import operator
import hmm
import numpy

imagePath = '/home/tiago/Desktop/simplecv.jpg'
#imagePath = '/home/tiago/ROS/catkin_ws/Image/camera_image.jpg'
filepath = "/tmp/output_graph.pb"

item = "apart"
 

def getBestObservation(list_observations, labels, last_five_percentages_observations):
			dic = {}
			for l in labels:
					dic[l] = 0
			for index, el in enumerate(list_observations):
					dic[el] = dic[el] + last_five_percentages_observations[index]
			return max(dic.iteritems(), key=operator.itemgetter(1))[0]

def get_labels():
    """Get a list of labels so we can see if it's an ad or not."""
    with open('/tmp/output_labels.txt', 'r') as fin:
        labels = [line.rstrip('\n') for line in fin]
    return labels

def run_classification():
		last_five_observations = []
		last_five_percentages_observations =[]
		#Initial State
		state = numpy.array([[1,0,0,0]])
		#cam = Camera(0)
		labels = get_labels()
		
		with tf.gfile.FastGFile(filepath, 'rb') as fin:
				graph_def = tf.GraphDef()
				graph_def.ParseFromString(fin.read())
				_ = tf.import_graph_def(graph_def, name='')

		with tf.Session() as sess:
				softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
				# And capture continuously forever.
				while True:
						#cam.getImage().save("simplecv.jpg")
						list_of_files = glob.glob('/home/tiago/ROS/catkin_ws/Images/First_Experience/*') # * means all if need specific format then *.csv
						imagePath = max(list_of_files, key=os.path.getctime)
						if not tf.gfile.Exists(imagePath):
								tf.logging.fatal('File does not exist %s', imagePath)
								return answer

						image_data = tf.gfile.FastGFile(imagePath, 'rb').read()
						# Make the prediction. Big thanks to this SO answer:
						# http://stackoverflow.com/questions/34484148/feeding-image-data-in-tensorflow-for-transfer-learning
						predictions = sess.run(softmax_tensor, {'DecodeJpeg/contents:0': image_data})
						prediction = predictions[0]

						# Get the highest confidence category.
						prediction = prediction.tolist()
						max_value = max(prediction)
						max_index = prediction.index(max_value)
						predicted_label = labels[max_index]
						last_five_percentages_observations.insert(0, max_value)
						last_five_observations.insert(0, predicted_label)
						if len(last_five_observations) == 5:
								bestObservation = getBestObservation(last_five_observations, labels, last_five_percentages_observations)
								print(bestObservation)
								state = hmm.getMostProbable(state, bestObservation)
								print state
								last_five_observations = []
								last_five_percentages_observations = []

if __name__ == '__main__':
			run_classification()
		
			  
			  
        
