__author__ = 'daniel'


from theano import tensor as T
from theano.tensor.shared_randomstreams import RandomStreams
from theano import function

# random stream object
srng = RandomStreams(seed=234)

# random uniform distribution
rnd_uniform = srng.uniform((2, 2))           # random uniform object
get_rnd_uniform = function([], rnd_uniform)  # getter function

