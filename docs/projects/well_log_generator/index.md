# Overview

Let's train a neural network to generate well logs! A generator can be used to interpolate missing data, or as implicit regularization for inversion.

Step 1: Find digital well logs for training. An easy way to download thousands of well logs in bulk is to get them from the [Kansas Geological Survey](http://www.kgs.ku.edu/PRS/Scans/Log_Summary/index.html).

Step 2: Prepare the data to use for training. We've gone through and selected just over 4000 wells to use as a training set. These are all the wells that have uninterrupted RILD logs in the depth interval from 400 ft to 4000 ft, sampled every foot. For a more tractable problem, we also downsampled this data by averaging linearly over 60 ft intervals, resulting in logs that have 60 data points each, spaced 60 ft apart. This downsampled training data is saved in a [Github repository](https://github.com/MLGeophysics/KGS_RILD_60ft).

Step 3: Choose a generator algorithm. There are a few ways to do this. One is to build a variational autoencoder, or VAE (see the [variational autoencoder project](https://mlgeophysics.github.io/community/projects/auto-encoder/vae/) for more). Another is to build a [generative adversarial network](https://mlgeophysics.github.io/community/projects/well_log_generator/GAN/) (GAN). Thirdly, we could combine the two to form a VAE-GAN; see [here](https://towardsdatascience.com/what-the-heck-are-vae-gans-17b86023588a) for an explanation. Ideally, let's try all three and compare the results!

