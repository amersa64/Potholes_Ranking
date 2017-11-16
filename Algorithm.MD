Let w, l, h be the dimensions of a pothole. Let d note the traffic density for that pothole:  
We define C as the scoring function:  
      **C(w,l,h,d) = w<sub>1</sub> * log(w * h * l+beta) + w<sub>2</sub> * ln(d)+e^(t)+   \sum_{i=1}^{10} t_i    **   
      where t is the time since recorded in years.  
      where G<sub>i</sub> is the report count for a location
      Where w1 and w2 are assigned weights for the density in that geolocation.  
beta is the base score which is subject to the constraint that w,l,h > alpha and d > lambda  
where alpha denote the threshold for a pothole dimension to be considered of concern.  
where lambda denotes the minimum traffic density for a pothole that would receive maintenance.  
(Again, lambda and alpha also depend on the city where this system is deployed)  
C would produce a score then we bin the potholes into bins ranging from seriousness 0-10 where 0 is not urgent and 10 is super urgent.  
Then we cluster the potholes of in the same bin based on location.
