from __future__ import absolute_import
from src.maze_manager import MazeManager
from src.maze import Maze

if __name__ == "__main__":
    manager = MazeManager()

    maze = manager.add_maze(10, 10)

    maze2 = Maze(10, 10)
    maze2 = manager.add_existing_maze(maze2, override=True)
    if isinstance(maze2, Maze):
        print(f"Added maze with ID {maze2.id}")

    maze_binTree = Maze(10, 10, algorithm="bin_tree")
    maze_binTree = manager.add_existing_maze(maze_binTree, override=True)
    if isinstance(maze_binTree, Maze):
        print(f"Added maze with Binary Tree algorithm with ID {maze_binTree.id}")

    manager.solve_maze(maze.id, "DepthFirstBacktracker")
    manager.set_filename("myFileName")

    manager.show_maze(maze.id)
    manager.show_generation_animation(maze.id)
    manager.show_solution_animation(maze.id)
    manager.show_solution(maze.id)
