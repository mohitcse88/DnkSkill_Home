import os

def fix_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Standardize Card Header/Container (Remove h-full)
    content = content.replace('bg-card flex flex-col h-full', 'bg-card flex flex-col')
    
    # Standardize Card Footer Spacing (Replace mt-auto with mt-6)
    content = content.replace('class="mt-auto flex flex-col', 'class="mt-6 flex flex-col')
    
    # Detailed Bullet Points (Synchronization)
    # DSA with C++
    if 'DSA with C++' in content:
        dsa_cpp_old = 'Beginner to Advanced'
        dsa_cpp_new = 'Beginner to Advanced</li><li class="flex items-start gap-2.5 text-[#374151] text-[15px] pb-1"><i data-lucide="check" class="text-primary shrink-0 mt-0.5" style="width: 18px; height: 18px;" stroke-width="2"></i>100+ Problems</li><li class="flex items-start gap-2.5 text-[#374151] text-[15px] pb-1"><i data-lucide="check" class="text-primary shrink-0 mt-0.5" style="width: 18px; height: 18px;" stroke-width="2"></i>Live Classes</li><li class="flex items-start gap-2.5 text-[#374151] text-[15px] pb-1"><i data-lucide="check" class="text-primary shrink-0 mt-0.5" style="width: 18px; height: 18px;" stroke-width="2"></i>Competitive Programming</li><li class="flex items-start gap-2.5 text-[#374151] text-[15px] pb-1"><i data-lucide="check" class="text-primary shrink-0 mt-0.5" style="width: 18px; height: 18px;" stroke-width="2"></i>Interview Prep'
        # To avoid duplicates if already present, we'd need more logic, but here we replace the simplified list.
        # Actually, let's just target the simplified 3-item list if it exists.
    
    # Web Development
    content = content.replace('Full Stack MERN', 'HTML, CSS, JavaScript</li><li class="flex items-start gap-2.5 text-[#374151] text-[15px] pb-1"><i data-lucide="check" class="text-primary shrink-0 mt-0.5" style="width: 18px; height: 18px;" stroke-width="2"></i>Git and GitHub</li><li class="flex items-start gap-2.5 text-[#374151] text-[15px] pb-1"><i data-lucide="check" class="text-primary shrink-0 mt-0.5" style="width: 18px; height: 18px;" stroke-width="2"></i>Nodejs, Expressjs, MongoDB</li><li class="flex items-start gap-2.5 text-[#374151] text-[15px] pb-1"><i data-lucide="check" class="text-primary shrink-0 mt-0.5" style="width: 18px; height: 18px;" stroke-width="2"></i>Reactjs</li><li class="flex items-start gap-2.5 text-[#374151] text-[15px] pb-1"><i data-lucide="check" class="text-primary shrink-0 mt-0.5" style="width: 18px; height: 18px;" stroke-width="2"></i>Deployment')
    
    # App Development
    content = content.replace('React Native & Flutter', 'JavaScript, TypeScript</li><li class="flex items-start gap-2.5 text-[#374151] text-[15px] pb-1"><i data-lucide="check" class="text-primary shrink-0 mt-0.5" style="width: 18px; height: 18px;" stroke-width="2"></i>Git and GitHub</li><li class="flex items-start gap-2.5 text-[#374151] text-[15px] pb-1"><i data-lucide="check" class="text-primary shrink-0 mt-0.5" style="width: 18px; height: 18px;" stroke-width="2"></i>Expo, React Native CLI</li><li class="flex items-start gap-2.5 text-[#374151] text-[15px] pb-1"><i data-lucide="check" class="text-primary shrink-0 mt-0.5" style="width: 18px; height: 18px;" stroke-width="2"></i>React Navigation, Redux</li><li class="flex items-start gap-2.5 text-[#374151] text-[15px] pb-1"><i data-lucide="check" class="text-primary shrink-0 mt-0.5" style="width: 18px; height: 18px;" stroke-width="2"></i>Build, Test, Deploy')
    
    # Data Science
    content = content.replace('Python & Libraries</li>\n              <li class="flex items-start gap-2.5 text-[#374151] text-[15px] pb-1">\n                <i data-lucide="check" class="text-primary shrink-0 mt-0.5" style="width: 18px; height: 18px;"\n                  stroke-width="2"></i>\n                SQL for Data Science', 'Python & Libraries</li><li class="flex items-start gap-2.5 text-[#374151] text-[15px] pb-1"><i data-lucide="check" class="text-primary shrink-0 mt-0.5" style="width: 18px; height: 18px;" stroke-width="2"></i>Data Visualization</li><li class="flex items-start gap-2.5 text-[#374151] text-[15px] pb-1"><i data-lucide="check" class="text-primary shrink-0 mt-0.5" style="width: 18px; height: 18px;" stroke-width="2"></i>SQL for Data Science</li><li class="flex items-start gap-2.5 text-[#374151] text-[15px] pb-1"><i data-lucide="check" class="text-primary shrink-0 mt-0.5" style="width: 18px; height: 18px;" stroke-width="2"></i>Statistical Analysis</li><li class="flex items-start gap-2.5 text-[#374151] text-[15px] pb-1"><i data-lucide="check" class="text-primary shrink-0 mt-0.5" style="width: 18px; height: 18px;" stroke-width="2"></i>Capstone Project')

    # DSA with Java
    content = content.replace('Core Java Mastery', 'Core Java Concepts</li><li class="flex items-start gap-2.5 text-[#374151] text-[15px] pb-1"><i data-lucide="check" class="text-primary shrink-0 mt-0.5" style="width: 18px; height: 18px;" stroke-width="2"></i>Collections Framework</li><li class="flex items-start gap-2.5 text-[#374151] text-[15px] pb-1"><i data-lucide="check" class="text-primary shrink-0 mt-0.5" style="width: 18px; height: 18px;" stroke-width="2"></i>Graph & Tree Algorithms</li><li class="flex items-start gap-2.5 text-[#374151] text-[15px] pb-1"><i data-lucide="check" class="text-primary shrink-0 mt-0.5" style="width: 18px; height: 18px;" stroke-width="2"></i>Dynamic Programming</li><li class="flex items-start gap-2.5 text-[#374151] text-[15px] pb-1"><i data-lucide="check" class="text-primary shrink-0 mt-0.5" style="width: 18px; height: 18px;" stroke-width="2"></i>Mock Interviews')

    # AI / ML
    content = content.replace('Machine Learning</li>\n              <li class="flex items-start gap-2.5 text-[#374151] text-[15px] pb-1">\n                <i data-lucide="check" class="text-primary shrink-0 mt-0.5" style="width: 18px; height: 18px;"\n                  stroke-width="2"></i>\n                Deep Learning', 'Neural Networks & Deep Learning</li><li class="flex items-start gap-2.5 text-[#374151] text-[15px] pb-1"><i data-lucide="check" class="text-primary shrink-0 mt-0.5" style="width: 18px; height: 18px;" stroke-width="2"></i>TensorFlow & PyTorch</li><li class="flex items-start gap-2.5 text-[#374151] text-[15px] pb-1"><i data-lucide="check" class="text-primary shrink-0 mt-0.5" style="width: 18px; height: 18px;" stroke-width="2"></i>Computer Vision Basics</li><li class="flex items-start gap-2.5 text-[#374151] text-[15px] pb-1"><i data-lucide="check" class="text-primary shrink-0 mt-0.5" style="width: 18px; height: 18px;" stroke-width="2"></i>Natural Language Processing</li><li class="flex items-start gap-2.5 text-[#374151] text-[15px] pb-1"><i data-lucide="check" class="text-primary shrink-0 mt-0.5" style="width: 18px; height: 18px;" stroke-width="2"></i>Real-World Case Studies')

    # Final polish: remove duplicate Placement & Interview Support if it got doubled
    # (Simplified replacement might cause it, so let's clean up)
    # Actually, the python replace is literal, so it should be fine if targets are unique.

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

fix_file(r'c:\Users\rohit\OneDrive\Desktop\simply-same-showcase-main\index.html')
fix_file(r'c:\Users\rohit\OneDrive\Desktop\simply-same-showcase-main\training\index.html')
print("Done")
