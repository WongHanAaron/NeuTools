# Developer Resources
Collection of resources for us developers!

## Table of Contents
1. [Neural Network Primer](#neural-network-primer)
2. [Git Resources](#git-resources)
3. [Tkinter / CustomTkinter Resources](#tkinter--customtkinter-resources)

# Neural Network Primer
Neural networks are a type of machine learning model that uses what is called a series 'perception' structures that can be trained to perform a task. 

The training process involves taking a set of training data (for example images), and continually performing a training process on the neural network model. For neural networks, this involves taking the data that is available, splitting it between a training set (usually 70% of the data) and a testing/validation set (the remainder). 

### Links
- [Neural Networks Simplified](https://towardsdatascience.com/neuralnetworks-implementation-d55cc6fc2f62)

## Convolutional Neural Networks
Convolutional Neural Networks

# Git Resources
### Links
- [Git with Visual Studio Code](https://www.youtube.com/watch?v=i_23KUAEtUM)

# Tkinter / CustomTkinter Resources
### General Links
- [Modern GUI using Tkinter](https://medium.com/@fareedkhandev/modern-gui-using-tkinter-12da0b983e22)
- [Updating Live Data with Tkinter](https://pythonprogramming.net/plotting-live-bitcoin-price-data-tkinter-matplotlib/)

### Tkinter Widget/Layouts Guides
Tkinter Widgets are the UI components that can be added to your UI
- [Using Tkinter Frame](https://www.tutorialspoint.com/python/tk_frame.htm)
- [Grid Layout Manager](https://www.pythonguis.com/tutorials/create-ui-with-tkinter-grid-layout-manager/)
- [Menubar](https://pythonspot.com/tk-menubar/)


# Python Multi-Threading and Multi-Processing
Most implementations of python do not support multi-threading which is often necessary to run multiple sections of code concurrently within a single program. For our use-case, we will at the very least need a thread to run the UI and a thread to run the training and inference. 
[More on Python not having Multi-threading](https://www.tutorialspoint.com/python-and-multi-threading-is-it-a-good-idea#:~:text=Python%20doesn't%20support%20multi,GIL%20does%20not%20prevent%20threading.).

To enable this, we will need to implement multi-processing that will allow for multiple instances of python to execute in different processes. The following resources below are on multi-processing and communication between the processes.

### Links
- [Multi-Processing with Message Passing](https://pymotw.com/2/multiprocessing/communication.html#:~:text=A%20simple%20way%20to%20communicate,can%20pass%20through%20a%20Queue.&text=This%20short%20example%20only%20passes,for%20the%20worker%20to%20finish.)
