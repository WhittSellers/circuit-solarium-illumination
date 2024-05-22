<p><a target="_blank" href="https://app.eraser.io/workspace/k5siHvgRpmN836RMQbUQ" id="edit-in-eraser-github-link"><img alt="Edit in Eraser" src="https://firebasestorage.googleapis.com/v0/b/second-petal-295822.appspot.com/o/images%2Fgithub%2FOpen%20in%20Eraser.svg?alt=media&amp;token=968381c8-a7e7-472a-8ed6-4a6626da5501"></a></p>

# circuit-solarium-illumination
Project for Circuit Solarium's interactive stage installation for Illumination NYC 2024. 

![20.jpg](/.eraser/k5siHvgRpmN836RMQbUQ___tTtaXijJXwZgula4by2oOh994aM2___OgGJYF3OLo2SbCAVhfZ3b.jpg "20.jpg")

![14.jpg](/.eraser/k5siHvgRpmN836RMQbUQ___tTtaXijJXwZgula4by2oOh994aM2___eTwWxSWZTIunkmF3QiAS-.jpg "14.jpg")



Below is a diagram of our hardware and software setup for the stage. We used 3 computers networked together in order to distribute computation tasks as best we could before consolidating visual output onto a single machine and finally outputting to the projectors.

![Figure 1](/.eraser/k5siHvgRpmN836RMQbUQ___tTtaXijJXwZgula4by2oOh994aM2___---figure---Jtd_CDYMbYy50Q-CkFcNF---figure---_7b4C2V-_GObkPn3lqmtCg.png "Figure 1")

Whitt's Desktop ran his Unreal Engine experience featuring a digital twin of the stage, virtual set pieces, and interactive VFX. Jon's laptop ran his TouchDesigner project using a webcam feed for light painting and mediapipe body tracking effects, with output textures and data shared over the network to the desktop. Whitt's Laptop ran MicrodoseVR as a third visual program to layer with visuals from the other two computers, or to use when no performers were on stage. Visual output from this program were also shared over the network back to Whitt's desktop, which used OBS to manage which visuals were being output to the projectors.



The TouchDesigner project on Whitt's Desktop analysis data from the VR trackers on his Dragon Staff, and acts as a pass through for osc messages coming from Jon's laptop to reduce the number of active osc servers in Whitt's UE experience. There is the beginnings of a Chataigne project in the repo for communicating with the staff LEDs, but ultimately this wasn't used during the show as we are able to dedicate enough time to building it out.

The following assets from Sketchfab were used in the Unreal Engine project.
"Small Greenhouse" (https://skfb.ly/o6TCo) by Mr. Trevor is licensed under Creative Commons Attribution (http://creativecommons.org/licenses/by/4.0/).
"Aquatic Room [Metashape + RC]" (https://skfb.ly/6XWHX) by Thomas Flynn is licensed under Creative Commons Attribution-NonCommercial (http://creativecommons.org/licenses/by-nc/4.0/).

<!--- Eraser file: https://app.eraser.io/workspace/k5siHvgRpmN836RMQbUQ --->
