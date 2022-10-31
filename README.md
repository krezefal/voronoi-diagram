# Voronoi diagram drawer

The Voronoi diagram of a finite set of points *S* in the plane represents a partition
of the plane such that each region of this partition forms a set of points that are
closer to one of the elements of the set S than to any other element of the set. 
Points here are base stations.

### Usage

The program is a CLI app written in Python 3.10, which draws the Voronoi diagram by 
the provided argument: **path to the image**. The image must be a schematic 
representation of the base stations' location, where each station is a black pixel.

```
python3 voronoi.py ~/image.png
```

Or it can be used w/o arguments: then the program will ask you about the field size 
and the number of base stations.


### Example of the result

<p align="center">
    <img src="example-img/tmp5dvgl5yh.PNG" alt />
</p>
