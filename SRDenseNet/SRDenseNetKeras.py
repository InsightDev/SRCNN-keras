# -*- coding: utf-8 -*-


from tensorflow.python.keras.models import Model;
from tensorflow.python.keras.optimizers import Adam;
from tensorflow.python.keras.layers.merge import concatenate;
from tensorflow.python.keras.engine.input_layer import Input;
from tensorflow.python.keras.layers.convolutional import Conv2D;
from tensorflow.python.keras.layers.convolutional import Conv2DTranspose;
from tensorflow.python.keras.utils.vis_utils import plot_model;


def SRDenseNetBlock(inputs, i, nlayers):
	logits = Conv2D(filters=16, kernel_size=3, padding="same", activation="relu",
					use_bias=True, name="conv2d_%d_%d" % (i + 1, 0 + 1))(inputs);

	for j in xrange(1, nlayers):
		middle = Conv2D(filters=16, kernel_size=3, padding="same", activation="relu",
						use_bias=True, name="conv2d_%d_%d" % (i + 1, j + 1))(logits);
		logits = concatenate([logits, middle], name="concatenate_%d_%d" % (i + 1, j + 1));

	return logits;


def SRDenseNetKeras(inputs, nblocks=8, nlayers=8):
	logits = Conv2D(filters=16, kernel_size=3, strides=1,
			padding='same', activation="relu", use_bias=True)(inputs);

	gggggg = logits;

	for i in xrange(nblocks):
		logits = SRDenseNetBlock(logits, i, nlayers);
		logits = concatenate([logits, gggggg]);

	logits = Conv2D(filters=256, kernel_size=1, padding='same',
				activation="relu", use_bias=True)(logits);

	logits = Conv2DTranspose(filters=256, kernel_size=3, strides=2,
			padding='same', activation="relu", use_bias=True)(logits);
	logits = Conv2DTranspose(filters=256, kernel_size=3, strides=2,
			padding='same', activation="relu", use_bias=True)(logits);

	logits = Conv2D(filters=1, kernel_size=3, padding='same', use_bias=True)(logits);

	mModel = Model(inputs, logits);
	mModel.compile(optimizer=Adam(lr=0.00001),
				loss='mean_squared_error',
				metrics=['mean_squared_error']);

	return mModel;


if __name__ == "__main__":
	inputs = Input(shape=(32, 32, 1));
	mModel = SRDenseNetKeras(inputs);
	print mModel.summary();
	plot_model(mModel, to_file='SRDenseNet.png', show_shapes=True);
	
	