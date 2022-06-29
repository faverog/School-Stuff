from cmd import Cmd
from enum import Enum
from operator import xor
import sys
import traceback

class r_extra(Enum):
    '''
    Extra values for r type instructions
    '''
    add     = 0
    sub     = 1
    slt     = 2
    syscall = 3
    Or      = 4
    And     = 5

class imm_opcode(Enum):
    '''
    Opcodes for i type instructions
    '''
    addi    = 6
    slti    = 11
    ori     = 7
    andi    = 2
    lw      = 8
    sw      = 13
    beq     = 1
    bne     = 15

# Opcode for r type instruction
r_type_opcode = 5

# Opcode for j type instruction
j_type_opcode = 4

class r_type:
    def __init__(self, extra, rd, rs, rt):
        self.opcode = format(r_type_opcode, '04b')
        self.rd = format(rd, '03b')
        self.rs = format(rs, '03b')
        self.rt = format(rt, '03b')
        self.extra = format(int(extra), '03b')
        self.output_instruction()

    def output_instruction(self):
        instruction = self.opcode + self.rs + self.rt + self.rd + self.extra
        instruction = '%0*X' % ((len(instruction) + 3) // 4, int(instruction, 2))
        print("Hex: " + instruction + '\n')

class imm_type:
    def __init__(self, opcode, rt, rs, imm):
        self.opcode = format(int(opcode), '04b')
        self.imm = self.get_imm(int(imm))
        self.rs = format(rs, '03b')
        self.rt = format(rt, '03b')
        self.output_instruction()

    def get_imm(self, imm):
        if imm < 0:
            # Get 2s complement
            imm *= -1
            xor_val = 63
            imm = format(xor(imm,xor_val) + 1, '06b')
        else:
            imm = format(imm, '06b')
        
        return imm

    def output_instruction(self):
        instruction = self.opcode + self.rs + self.rt + self.imm
        instruction = '%0*X' % ((len(instruction) + 3) // 4, int(instruction, 2))
        print("Hex: " + instruction + '\n')

class j_type:
    def __init__(self, absolute):
        self.opcode = format(j_type_opcode, '04b')
        self.absolute = format(int(absolute), '012b')
        self.output_instruction()

    def output_instruction(self):
        instruction = self.opcode + self.absolute
        instruction = '%0*X' % ((len(instruction) + 3) // 4, int(instruction, 2))
        print("Hex: " + instruction + '\n')

class ROMInstructionsShell(Cmd):
    """
    A class used to provide a command-line interface with the ROM Instructor
    """
    intro = "Assignment 7 ROM Instructions, 2022. Type help or ? to list commands.\n"
    prompt = "Mnemonic> "

    def __init__(self):
        super().__init__(self)

    def do_add(self, args):
        """
        ADD: Rd, Rs, Rt
        """
        try:
            args_list = args.split()
            rd = int(args_list[0])
            rs = int(args_list[1])
            rt = int(args_list[2])

            r_type(r_extra.add.value, rd, rs, rt)
        except:
            print(traceback.format_exc())
            return

    def do_sub(self, args):
        """
        SUB: Rd, Rs, Rt
        """
        try:
            args_list = args.split()
            rd = int(args_list[0])
            rs = int(args_list[1])
            rt = int(args_list[2])

            r_type(r_extra.sub.value, rd, rs, rt)
        except:
            print(traceback.format_exc())
            return

    def do_slt(self, args):
        """
        SLT: Rd, Rs, Rt
        """
        try:
            args_list = args.split()
            rd = int(args_list[0])
            rs = int(args_list[1])
            rt = int(args_list[2])

            r_type(r_extra.slt.value, rd, rs, rt)
        except:
            print(traceback.format_exc())
            return

    def do_syscall(self, args):
        """
        SYSCALL: Rd, Rs, Rt
        """
        try:
            args_list = args.split()
            rd = int(args_list[0])
            rs = int(args_list[1])
            rt = int(args_list[2])

            r_type(r_extra.syscall.value, rd, rs, rt)
        except:
            print(traceback.format_exc())
            return

    def do_or(self, args):
        """
        OR: Rd, Rs, Rt
        """
        try:
            args_list = args.split()
            rd = int(args_list[0])
            rs = int(args_list[1])
            rt = int(args_list[2])

            r_type(r_extra.Or.value, rd, rs, rt)
        except:
            print(traceback.format_exc())
            return

    def do_and(self, args):
        """
        AND: Rd, Rs, Rt
        """
        try:
            args_list = args.split()
            rd = int(args_list[0])
            rs = int(args_list[1])
            rt = int(args_list[2])

            r_type(r_extra.And.value, rd, rs, rt)
        except:
            print(traceback.format_exc())
            return

    def do_addi(self, args):
        """
        ADDI: Rt, Rs, imm/simm
        """
        try:
            args_list = args.split()
            rt = int(args_list[0])
            rs = int(args_list[1])
            imm = int(args_list[2])

            imm_type(imm_opcode.addi.value, rt, rs, imm)
        except:
            print(traceback.format_exc())
            return

    def do_slti(self, args):
        """
        SLTI: Rt, Rs, imm/simm
        """
        try:
            args_list = args.split()
            rt = int(args_list[0])
            rs = int(args_list[1])
            imm = int(args_list[2])

            imm_type(imm_opcode.slti.value, rt, rs, imm)
        except:
            return

    def do_ori(self, args):
        """
        ORI: Rt, Rs, imm/simm
        """
        try:
            args_list = args.split()
            rt = int(args_list[0])
            rs = int(args_list[1])
            imm = int(args_list[2])

            imm_type(imm_opcode.ori.value, rt, rs, imm)
        except:
            return

    def do_andi(self, args):
        """
        ANDI: Rt, Rs, imm/simm
        """
        try:
            args_list = args.split()
            rt = int(args_list[0])
            rs = int(args_list[1])
            imm = int(args_list[2])

            imm_type(imm_opcode.andi.value, rt, rs, imm)
        except:
            return

    def do_lw(self, args):
        """
        LW: Rt, Rs, imm/simm
        """
        try:
            args_list = args.split()
            rt = int(args_list[0])
            rs = int(args_list[1])
            imm = int(args_list[2])

            imm_type(imm_opcode.lw.value, rt, rs, imm)
        except:
            return

    def do_sw(self, args):
        """
        SW: Rt, Rs, imm/simm
        """
        try:
            args_list = args.split()
            rt = int(args_list[0])
            rs = int(args_list[1])
            imm = int(args_list[2])

            imm_type(imm_opcode.sw.value, rt, rs, imm)
        except:
            return

    def do_beq(self, args):
        """
        BEQ: Rt, Rs, imm/simm
        """
        try:
            args_list = args.split()
            rt = int(args_list[0])
            rs = int(args_list[1])
            imm = int(args_list[2])

            imm_type(imm_opcode.beq.value, rt, rs, imm)
        except:
            return

    def do_bne(self, args):
        """
        BNE: Rt, Rs, imm/simm
        """
        try:
            args_list = args.split()
            rt = int(args_list[0])
            rs = int(args_list[1])
            imm = int(args_list[2])

            imm_type(imm_opcode.bne.value, rt, rs, imm)
        except:
            return

    def do_j(self, args):
        """
        J: absolute
        """
        try:
            args_list = args.split()
            absolute = int(args_list[0])

            j_type(absolute)
        except:
            return
    
    def do_exit(self, args):
        """
        Exit the Recipe Manager Shell
        """
        sys.exit()

def main():
    try:
        prompt = ROMInstructionsShell()
    except:
        print("Exiting...")
        sys.exit()
    prompt.cmdloop()

if __name__ == '__main__':
    main()



        
