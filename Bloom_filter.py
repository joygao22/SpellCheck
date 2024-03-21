import hashing
import heapq

class BloomFilter(object):

  def __init__(self, bloom_size, num_hash):
    self.size = bloom_size  # size of bloom filter
    self.num_hash = num_hash  # number of hash functions
    self.bit_array = [False] * bloom_size
    self.populated = False


  def addAscii(self, word, tableSize):
    letters = []
    for char in word:
      letters.append(char)
    hashRes = hashing.asciiHash(letters,tableSize)
    count = 0
    if not self.bit_array[int(hashRes)]:
      self.bit_array[int(hashRes)] = True
      count += 1
    return count

  def addJenkins(self, word, tableSize):
    letters = []
    for char in word:
      letters.append(char)
    hashRes = hashing.jenkinsHash(letters, tableSize)
    count = 0
    if self.bit_array[int(hashRes)] == False:
      self.bit_array[int(hashRes)] = True
      count += 1
    return count

  def addDivision(self, word, seed, tableSize):
    letters = []
    for char in word:
      letters.append(char)
    hashRes = hashing.divisionHash(letters, seed, tableSize)
    count = 0
    if self.bit_array[int(hashRes)] == False:
      self.bit_array[int(hashRes)] = True
      count += 1
    return count

  def addFnv1a(self, word, seed, tableSize):
    hashRes = hashing.fnv1aHash(word, seed, tableSize)
    count = 0
    if self.bit_array[int(hashRes)] == False:
      self.bit_array[int(hashRes)] = True
      count += 1
    return count

  def query(self, item, tableSize):
    letters = []
    for char in item:
      letters.append(char)
    ascii_hash = hashing.asciiHash(letters, tableSize)
    if self.bit_array[int(ascii_hash)] == False:
      return False;

    jenkins_hash = hashing.jenkinsHash(letters, tableSize)
    if self.bit_array[int(jenkins_hash)] == False:
      return False;
    for i in range(10):
      division_hash = hashing.divisionHash(letters, i, tableSize)
      if self.bit_array[int(division_hash)] == False:
        return False;
    for j in range(10):
      fnv1a_hash = hashing.fnv1aHash(item, i, tableSize)
      if self.bit_array[int(fnv1a_hash)] == False:
        return False;
    return True

  def is_populated(self):
    return self.populated

class BKNode:
  def __init__(self, word):
    self.word = word
    self.children = []

  def add_child(self, child_node, distance):
    self.children.append((distance, child_node))

  def __repr__(self):
    return f"BKNode({self.word})"

class BKTree:
  def __init__(self, distance_metric):
    self.root = None
    self.distance_metric = distance_metric
    self.populatedFlag = False

  def is_populated(self):
    return self.populatedFlag

  def insert(self, word):
    if self.root is None:
      self.root = BKNode(word)
      return

    parent = None
    current_node = self.root
    while current_node:
      distance = self.distance_metric(current_node.word, word)
      if distance == 0:
        return
      if distance in [d for d, _ in current_node.children]:
        parent = current_node
        current_node = [child for d, child in current_node.children if d == distance][0]
      else:
        new_node = BKNode(word)
        current_node.add_child(new_node, distance)
        return

  def find_k_closest(self, word, k):
    if self.root is None:
        return []

    candidates = [self.root]
    closestWords = []

    while candidates:
        current_node = candidates.pop(0)
        distance = self.distance_metric(current_node.word, word)
        heapq.heappush(closestWords, (distance, current_node.word))

        minDistance = closestWords[0][0]

        for dist, child in current_node.children:
            if distance - k <= dist <= distance + k:
                candidates.append(child)

        while closestWords and closestWords[0][0] > minDistance + k:
            heapq.heappop(closestWords)

    closestWords.sort(key=lambda x: x[0])

    # Create a dictionary to group words by distance
    distance_groups = {}
    for dist, word in closestWords:
        if dist not in distance_groups:
            distance_groups[dist] = []
        distance_groups[dist].append(word)


    for dist in distance_groups:
        distance_groups[dist].sort(reverse=True)

    ordered_words = [word for dist in sorted(distance_groups.keys()) for word in distance_groups[dist]]

    ordered_words = ordered_words[:k]

    return str(ordered_words)



