Der Docker muss mit den Device-Berechtigungen aufgerufen werden.
docker run -it --device=/dev/input/js0 ros:noetic
