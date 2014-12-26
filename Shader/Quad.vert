#version 330

uniform mat4 worldViewProjectionMatrix;

layout(location=0) in vec3 positionIn;
layout(location=1) in vec2 texcoordIn;

out vec2 texcoord;

void main() {
   gl_Position = worldViewProjectionMatrix * vec4(positionIn, 1);
   texcoord = texcoordIn;
}


