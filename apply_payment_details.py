import os
import glob

# The final, approved HTML block for the registration card
NEW_BLOCK = """            <div class="bg-white border border-[#e2e8f0] rounded-[24px] shadow-sm p-8 pb-5 max-w-md mx-auto relative z-10">


              <div class="mb-8">
                <h3 class="text-[20px] font-bold text-[#1e293b]">Payment Details</h3>
                <p class="text-[14px] text-[#64748b] mt-1 leading-snug">
                  (18% GST already included which is paid to the Government)
                </p>
                <div class="flex items-center gap-3 mt-3 flex-wrap">
                  <span class="text-[32px] font-extrabold text-[#0f172a]">₹ 1499</span>
                  <span class="text-[18px] text-[#94a3b8] line-through font-medium">₹ 6,999</span>
                  <span class="bg-emerald-50 text-emerald-700 text-[11px] font-bold px-2 py-0.5 rounded-[4px] border border-emerald-100 uppercase tracking-tight">78% OFF</span>
                </div>
              </div>

              <form id="enrollmentForm" class="space-y-5">
                <div class="space-y-2">
                  <label class="block text-[12px] font-bold text-[#334155] uppercase tracking-wide">Full Name</label>
                  <input type="text" placeholder="Enter your full name" class="w-full h-[56px] px-5 rounded-[12px] border border-[#cbd5e1] focus:border-[#2d6a4f] focus:ring-1 focus:ring-[#2d6a4f] outline-none transition-all placeholder:text-[#94a3b8]" required>
                </div>

                <div class="space-y-2">
                  <label class="block text-[12px] font-bold text-[#334155] uppercase tracking-wide">Phone Number</label>
                  <div class="flex h-[56px]">
                    <div class="flex items-center justify-center px-4 bg-[#f8fafc] border border-[#cbd5e1] border-r-0 rounded-l-[12px] text-[#475569] font-bold text-[15px]">
                      +91
                    </div>
                    <input type="tel" placeholder="10-digit number" class="flex-1 px-5 rounded-r-[12px] border border-[#cbd5e1] focus:border-[#2d6a4f] focus:ring-1 focus:ring-[#2d6a4f] outline-none transition-all placeholder:text-[#94a3b8]" required>
                  </div>
                </div>

                <div class="space-y-2">
                  <label class="block text-[12px] font-bold text-[#334155] uppercase tracking-wide">Email Address</label>
                  <input type="email" placeholder="you@example.com" class="w-full h-[56px] px-5 rounded-[12px] border border-[#cbd5e1] focus:border-[#2d6a4f] focus:ring-1 focus:ring-[#2d6a4f] outline-none transition-all placeholder:text-[#94a3b8]" required>
                </div>

                <div class="space-y-2">
                  <label class="block text-[12px] font-bold text-[#334155] uppercase tracking-wide">College / University Name</label>
                  <input type="text" placeholder="e.g. LPU, Jalandhar" class="w-full h-[56px] px-5 rounded-[12px] border border-[#cbd5e1] focus:border-[#347754] focus:ring-1 focus:ring-[#347754] outline-none transition-all placeholder:text-[#94a3b8]" required>
                </div>

                <button type="submit" class="w-full h-[60px] bg-[#2d6a4f] hover:bg-[#23533e] text-white font-bold text-[18px] rounded-[14px] flex items-center justify-center gap-3 transition-all mt-4 active:scale-[0.98] shadow-[0_10px_20px_-5px_rgba(45,106,79,0.3)]">
                  Pay ₹ 1499 <i data-lucide="arrow-right" class="w-5 h-5"></i>
                </button>
              </form>

              <div class="mt-4 flex items-center justify-center gap-2 text-[#94a3b8] text-[13px] font-medium border-t border-slate-50 pt-4">
                <i data-lucide="lock" class="w-4 h-4"></i>
                100% Safe & Secure Payment Space
              </div>
            </div>"""

def apply_to_file(filepath):
    print(f"Updating {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The block we are looking for starts with this specific class and tag
    # and ends after the secure payment space div
    start_marker = '<div class="bg-white border border-[#e2e8f0] rounded-[24px] shadow-sm p-8 max-w-md mx-auto relative z-10">'
    end_marker = '100% Safe & Secure Payment Space\n              </div>\n            </div>'
    
    # Try to find the block
    start_index = content.find(start_marker)
    if start_index == -1:
        print(f"  Warning: Start marker not found in {filepath}")
        return

    # Find the end of the 100% Safe div
    # Actually, let's look for the closing div chain
    end_index = content.find(end_marker, start_index)
    if end_index == -1:
        # Fallback for slightly different formatting
        end_marker_alt = '100% Safe & Secure Payment Space\r\n              </div>\r\n            </div>'
        end_index = content.find(end_marker_alt, start_index)
        if end_index == -1:
            print(f"  Warning: End marker not found in {filepath}")
            return
            
    # Calculate exactly where the block ends (after the last </div>)
    total_end = end_index + len(end_marker)
    
    new_content = content[:start_index] + NEW_BLOCK + content[total_end:]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

# Process all training and course pages
files = glob.glob('training/*/index.html') + glob.glob('courses/*/index.html')

for filepath in files:
    # Skip web-development as we already handled it manually and refined it
    if 'web-development' in filepath:
        continue
    apply_to_file(filepath)

print("Done! All enrollment forms updated.")
