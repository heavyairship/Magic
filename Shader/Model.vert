/*****************************************************************************
 * Simple, Fast Renderer (SFR)                                               *
 * CS249b                                                                    *
 * Matt Fichman                                                              *
 * February, 2011                                                            *
 *****************************************************************************/

#version 330 
layout(location=0) in vec3 positionIn;
//layout(location=1) in vec3 normalIn;
//layout(location=2) in vec3 tangentIn;
layout(location=3) in vec2 texcoordIn;

uniform mat4 worldViewProjectionMatrix;

/* Very fast simple solid-color shader for rendering to depth */
void main() {
	// Transform the vertex to get the clip-space position of the vertex
	gl_Position = worldViewProjectionMatrix * vec4(positionIn, 1);
}
