
list = ['a', 'b', 'c', 'a']
print(list)
#has index, ordered
print(list[2])
#lists are mutable (modifiable), can change after creation

tuple = ('a', 'b', 'c', 'a')
print(tuple)
#has index, ordered
print(tuple[3])
#lists are immutable (unmodifiable), can't change after creation; useful for info that doesn't change like birthdays


set = {'a', 'b', 'c', 'a'}
print(set)
# automatically drops duplicates, other two don't
# unordered, the other two are ordered. doesn't have index
# mutable