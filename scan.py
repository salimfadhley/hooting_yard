from git import Repo

def main():
    repo = Repo(".")

    master = repo.heads.master
    origin = repo.remotes.origin

    for f in repo.untracked_files:
        if f.endswith(".mp3"):
            print(f)
            repo.index.add([f])
            repo.index.commit(f"Automatically added {f}.")
            origin.push()

if __name__ == "__main__":
    main()