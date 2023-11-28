# viewing Transformation

1. World Coordinate: world coordinate die kono image computer memory te store kora hoy.

2. ekhon ei image ta kono display device er modhe dekhte hole we need Device Coordinate.

3. world coordinate er kono point/line jodi dispay device e dekhte chai, taile oi point/line ke map korte hobe device coordinate e. Ei mapping kei bole Viewing Transformation.

---------------------------------

# Window to Viewport Transformation

### Window

1. window thake world coordinate er modhe.

2. World Coordinate er jei area amra display'r jonno select korbo, oita hosse window.

### Viewport

1. ekhon viewport thake hosse Device Coordinate e

2. Device Coordinate er modhe jei area amra display kori, sheta hosse viewport.

### Transformation:

1. Winodow er ekta point(Xw, Yw) ke viewport e (Xv, Yv) dekhate hole, we need Normalized window coordinate.

---------

# point clipping:

* is used to find whether a particular point is inside the window or outside the window
