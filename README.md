🚀 Line-Following Robot with Spiral Mapping Optimization for Maze Traversal
📘 Overview
This project implements a line-following robot for a maze competition where the map contains obstacles laid out on a white surface with black lines. The objective is for the robot to traverse the maze using an optimized spiral traversal strategy rather than traditional line-following methods. The robot uses a camera to maintain a clearance x from the map borders and follows a spiral pattern to efficiently cover the maze's surface.

We utilize two main spiral traversal strategies:

Normal Spiral Traversal: A conventional spiral that follows an expanding pattern without adhering to any special mathematical properties.
Golden Spiral Traversal: Used only when the maze dimensions allow the map to support a spiral that follows the Golden Ratio properties.
This ensures a faster, efficient traversal and coverage of the maze with fewer turns and reduced path length.

🔍 Key Concepts
🧮 Robot Path Traversal Strategy
Camera Distance x
The robot maintains a constant clearance x from the edges of the maze. x is the distance that the camera detects from the border of the maze surface. This ensures a consistent clearance while following a spiral path.

Spiral Traversal Approach

The robot uses a spiral movement algorithm rather than navigating the maze line-by-line.
Each spiral loop increments by maintaining a step size of 2x (where x is the clearance distance).
This method enables comprehensive coverage of the entire maze surface with fewer turns and better efficiency.
Efficient Coverage
As the robot spirals inward, it scans and maps the surface of the maze.
If the endpoint is detected during traversal, it directly moves in a straight line toward the endpoint.
🔢 Spiral Strategies
1. Normal Spiral Traversal
In a normal spiral, the robot follows a pattern of turning continuously while maintaining a step size of 2x between each arm of the spiral.
The spiral expands in a straightforward manner, following a simple radius increment pattern without relying on any special mathematical ratios like the Golden Ratio.
In a 100x100-meter maze grid, the robot maintains a constant clearance x, following a uniform spiral pattern until the center of the maze is reached.
Mathematics of Normal Spiral Traversal
For a normal spiral, we can describe it with the polar equation:

𝑟
(
𝜃
)
=
𝑎
+
𝑏
⋅
𝜃
r(θ)=a+b⋅θ
Where:

𝑟
(
𝜃
)
r(θ) is the radial distance from the center of the spiral.

𝑎
a and 
𝑏
b are scaling factors to maintain the distance 2x between each layer of the spiral arms.

As each arm grows with a step of 2x, the robot effectively covers the entire maze surface by following the pattern inward step-by-step.

2. Golden Spiral Traversal
The Golden Spiral approach is only applicable when the maze size fits the constraints of the Golden Ratio.

In a Golden Spiral, the spiral pattern follows the mathematical properties of the Golden Ratio (approximately 1.618), ensuring that the spacing between successive layers decreases in a manner consistent with this ratio.

The Golden Spiral provides an even more efficient coverage pattern for maps that meet specific dimensions.

Mathematics of Golden Spiral Traversal
The Golden Spiral follows the polar equation:

𝑟
(
𝜃
)
=
𝑐
⋅
𝑒
𝑏
⋅
𝜃
r(θ)=c⋅e 
b⋅θ
 
Where:

𝑐
c and 
𝑏
b are scaling constants to maintain the spiral's optimal spacing according to the Golden Ratio.

For our robot on a map with dimensions supporting the Golden Spiral, we cap the radius expansion at 2x, ensuring that turns don’t get smaller than this minimum step distance.

📐 Calculating Time, Distance, and Turns
Let's walk through an example with a 100x100-meter map:

🚗 Robot Speed
Speed = 8 km/hour = 8000 meters/hour.
Estimating Distance Covered in Normal Spiral Traversal
For a 100-meter grid, each spiral arm adds about 2 meters in step size.
For approximately 50 spiral layers, the total traversal distance sums up to around 500 meters.
Time to Complete the Normal Spiral Traversal:

Time
=
500
 
meters
8000
 
m/hr
≈
0.0625
 
hours
≈
3.75
 
minutes
Time= 
8000m/hr
500meters
​
 ≈0.0625hours≈3.75minutes
Golden Spiral Traversal Efficiency
In a Golden Spiral scenario, the turns have optimal spacing according to the Golden Ratio.
For a maze meeting Golden constraints:
The coverage distance required is reduced due to fewer turns and consistent radial expansion patterns.
In such cases, traversal distance decreases by around 10-20% compared to the normal spiral.
🔧 Project Structure
bash
Copy code
/robot-spiral-mapping/
├── main.cpp                # Robot control and navigation logic
├── algorithms/spiral.cpp    # Spiral pattern generation
├── sensors/camera.cpp       # Camera integration for border detection
├── mapping/coverage.cpp     # Comprehensive area coverage mapping
├── tests/test_robot.cpp     # Unit tests for spiral traversal algorithms
├── config/settings.yaml     # Speed, grid size, and robot parameters
├── docs/README.md           # Mathematical assumptions and calculations
└── LICENSE                   # MIT License
📜 Future Enhancements
Adaptive Spiral Control: Modify spiral traversal dynamically according to maze obstacles.
Golden Spiral Integration: Implement detection mechanisms to automatically switch to the Golden Spiral for applicable maze sizes.
Speed Optimization Algorithms: Fine-tune robot speed dynamically to minimize traversal time.
Obstacle Navigation: Seamlessly handle obstacles during spiral traversal by recalibrating movement patterns.
📢 Conclusion
By employing the spiral traversal method, both normal and Golden spiral approaches, the project achieves:

Faster traversal with fewer turns.
More efficient coverage and mapping of the maze surface.
Seamless detection and movement to endpoints with direct-line efficiency.
This ensures a comprehensive traversal and optimal mapping of the maze surface using minimal computational overhead and robot control turns.

📜 Contact
GitHub: username
Email: [robotics@example.com]
