#list
animes = ["Naruto", "One Piece", "Attack on Titan", "Demon Slayer", "Death Note"]
print(animes)

print(type(animes))

#accessing elements of list

print(animes[0])
print(animes[0:2])
print(animes[-1])
print(animes[-3])

#list functions

animes.append("Jujutsu Kaisen")
print(animes)

animes.insert(1, "Bleach")
print(animes)

animes.remove("Death Note")
print(animes)

animes.pop()
print(animes)

animes.sort()
print(animes)

animes.reverse()
print(animes)

print(len(animes))

if "Naruto" in animes:
    print("Naruto is in the list")

#loop

for anime in animes:
    print(anime)

for item in animes:
  print(item, len(item))

for item in animes:
  print(item, item.upper())

#lets create new lists 

names = [['sanket','yash','aditya'], ['pritam', 'chaitany']]
print(names)
print(len(names))

print(names[0])
print(names[1])

print(names[0], type(names[0]))
print(names[1], type(names[1]))