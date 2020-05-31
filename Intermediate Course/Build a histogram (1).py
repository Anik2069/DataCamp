# Create histogram of life_exp data
import matplotlib.pyplot as plt
plt.hist(life_exp,bins=10) 

# Display histogram
plt.show()

#Part 2
# Build histogram with 5 bins

plt.hist(life_exp,bins=5)

# Show and clean up plot
plt.show()
plt.clf()

# Build histogram with 20 bins
plt.hist(life_exp,bins=20)


# Show and clean up again
plt.show()
plt.clf()