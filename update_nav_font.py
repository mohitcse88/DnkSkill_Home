import os
import glob

def update_nav_font(filepath):
    print(f"Updating nav font in {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Targets specifically the navigation link font classes
    # We look for common patterns in these files
    patterns = [
        ('font-medium" mobile-link', 'font-semibold" mobile-link'),
        ('transition-colors font-medium">Home</a>', 'transition-colors font-semibold">Home</a>'),
        ('transition-colors font-medium">Training</a>', 'transition-colors font-semibold">Training</a>'),
        ('transition-colors font-medium">Courses</a>', 'transition-colors font-semibold">Courses</a>'),
        ('transition-colors font-medium">About</a>', 'transition-colors font-semibold">About</a>'),
        ('text-primary font-medium mobile-link', 'text-primary font-semibold mobile-link'),
        ('text-foreground font-medium mobile-link', 'text-foreground font-semibold mobile-link'),
    ]
    
    updated_content = content
    for old, new in patterns:
        updated_content = updated_content.replace(old, new)
        
    if updated_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        return True
    return False

# List all relevant files
all_files = [
    'index.html',
    'about/index.html',
    'training/index.html',
    'courses/index.html',
]
# Add subdirectories
all_files.extend(glob.glob('training/*/index.html'))
all_files.extend(glob.glob('courses/*/index.html'))

count = 0
for fpath in all_files:
    if os.path.exists(fpath):
        if update_nav_font(fpath):
            count += 1

print(f"Done! {count} files updated with semibold navigation font.")
