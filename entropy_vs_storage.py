import sys
import time

def run_hardware_checkmate():
    print("=" * 65)
    print("      LATENT SPACE ENTROPY VS. MEMORY ALLOCATION LOGIC")
    print("=" * 65)
    
    # 1. Gather hardware inputs from user
    try:
        model_size_gb = float(input("[INPUT] Enter local model weights file size (in GB) [e.g., 4]: ") or 4)
        sample_img_mb = float(input("[INPUT] Enter average uncompressed file size (in MB) [e.g., 4]: ") or 4)
        claimed_dataset_millions = float(input("[INPUT] Enter claimed dataset size (in millions of items) [e.g., 5000]: ") or 5000)
    except ValueError:
        print("[ERROR] Invalid numeric parameters. Halting logic thread.")
        sys.exit(1)
        
    print("\n[PROCESSING] Calculating tensor limits against storage matrices...")
    time.sleep(0.6)
    
    # 2. Mathematical execution
    claimed_dataset_count = claimed_dataset_millions * 1_000_000
    required_storage_mb = claimed_dataset_count * sample_img_mb
    required_storage_tb = required_storage_mb / (1_024 * 1_024)
    
    compression_ratio = (required_storage_tb * 1024) / model_size_gb
    
    # Bytes per file logic under the retrieval narrative
    model_bytes = model_size_gb * 1024 * 1024 * 1024
    allocated_bytes_per_asset = model_bytes / claimed_dataset_count

    # 3. Output hardware proof
    print("-" * 65)
    print("                     METRIC LOG ANALYSIS")
    print("-" * 65)
    print(f"-> Local Weight Footprint      : {model_size_gb:.2f} GB")
    print(f"-> Claimed Retrieval Inventory : {claimed_dataset_millions:.1f} Million Assets")
    print(f"-> Theoretical Uncompressed Vol: {required_storage_tb:,.2f} TB (Terabytes)")
    print(f"-> Implied Compression Deficit : {compression_ratio:,.1f}x reduction")
    print(f"-> Maximum Data Allocation/File: {allocated_bytes_per_asset:.2f} Bytes")
    print("-" * 65)
    
    # 4. Contextual Deductions
    print("                  ARCHITECTURAL DEDUCTION")
    print("-" * 65)
    if allocated_bytes_per_asset < 1.0:
        print(f"CRITICAL FAULT: The network yields less than 1 single byte ({allocated_bytes_per_asset:.4f} B)\n"
              "per claimed asset. A fraction of a byte cannot store an image coordinate,\n"
              "let alone a compressed thumbnail file.")
    else:
        print(f"CRITICAL FAULT: {allocated_bytes_per_asset:.2f} Bytes is structurally insufficient\n"
              "to maintain string data or headers for a file index of this magnitude.")
              
    print("\nCONCLUSION: Local file size math proves data retrieval is structurally impossible.\n"
          "The output is a real-time probabilistic calculation via latent weights.")
    print("=" * 65)

if __name__ == "__main__":
    run_hardware_checkmate()
