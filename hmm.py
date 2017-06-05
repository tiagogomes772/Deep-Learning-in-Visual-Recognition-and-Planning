import numpy
from fractions import Fraction

#Transition Probabilities
transition_matrix = numpy.array([[15.0/19.0, 2.0/19.0, 2.0/19.0, 0],
																 [0, 6.0/8.0, 0, 2.0/8.0],
																 [0, 0, 7.0/9.0, 2.0/9.0],
																 [0, 0, 0, 1]])
																 
#Emission Probabilities -> To get real values
emission_matrix = numpy.array([[244.0/291.0, 23/326.3, 17/324.2, 2/197.7],
															 [25.0/291.0, 263.3/326.3, 36/324.2, 5/197.7],
															 [16/291.0, 31/326.3, 250.2/324.2, 16/197.7],
															 [6/291.0, 9/326.3, 21/324.2, 174.7/197.7]])

#diag of observation given the emission matrix



def getMostProbable(init_probability, obs_state):

		if obs_state == "apart":
				diag = numpy.diag(emission_matrix[:,0])
		elif obs_state == "headmissing" :
				diag = numpy.diag(emission_matrix[:,1])
		elif obs_state == "shouldermissing" :
				diag = numpy.diag(emission_matrix[:,2])
		else :
				diag = numpy.diag(emission_matrix[:,3])
						
		#print(init_probability.shape)
		#print(transition_matrix.shape)
		#print(emission_matrix.shape)
		
		init_transition_matrix = numpy.dot(init_probability,transition_matrix)
		new_probability = numpy.dot(init_transition_matrix,diag)
		return new_probability


